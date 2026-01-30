#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
from collections import defaultdict, Counter
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        tree = [[] for _ in range(n)]
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))

        self.max_length = 0
        self.min_nodes = float('inf')

        def dfs(node, parent, val_counter, duplicated, length, nodes):
            val = nums[node]
            val_counter[val] += 1
            if val_counter[val] == 2:
                if duplicated:
                    val_counter[val] -= 1
                    return
                else:
                    duplicated = True
            elif val_counter[val] > 2:
                val_counter[val] -= 1
                return
            # Update answer
            if length > self.max_length:
                self.max_length = length
                self.min_nodes = nodes
            elif length == self.max_length:
                self.min_nodes = min(self.min_nodes, nodes)
            for nei, w in tree[node]:
                if nei != parent:
                    dfs(nei, node, val_counter, duplicated, length + w, nodes + 1)
            val_counter[val] -= 1

        dfs(0, -1, Counter(), False, 0, 1)
        return [self.max_length, self.min_nodes]
# @lc code=end