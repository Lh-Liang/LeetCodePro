#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict
        n = len(nums)
        tree = defaultdict(list)
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))

        self.max_len = 0
        self.min_nodes = float('inf')

        def dfs(u, parent, seen, cur_len, cur_nodes):
            val = nums[u]
            if val in seen:
                # Not a valid path
                return
            seen.add(val)
            # Update answer if needed
            if cur_len > self.max_len:
                self.max_len = cur_len
                self.min_nodes = cur_nodes
            elif cur_len == self.max_len:
                self.min_nodes = min(self.min_nodes, cur_nodes)
            for v, w in tree[u]:
                if v == parent:
                    continue
                dfs(v, u, seen, cur_len + w, cur_nodes + 1)
            seen.remove(val)

        dfs(0, -1, set(), 0, 1)
        return [self.max_len, self.min_nodes]
# @lc code=end