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
        for u, v, length in edges:
            tree[u].append((v, length))
            tree[v].append((u, length))

        max_length = 0
        min_nodes = float('inf')

        def dfs(u, parent, seen, cur_len, cur_nodes):
            nonlocal max_length, min_nodes
            if nums[u] in seen:
                return
            seen.add(nums[u])
            # Verify constraints before updating global results
            if cur_len > max_length:
                max_length = cur_len
                min_nodes = cur_nodes
            elif cur_len == max_length:
                min_nodes = min(min_nodes, cur_nodes)
            for v, w in tree[u]:
                if v == parent:
                    continue  # Maintain downward direction
                dfs(v, u, seen, cur_len + w, cur_nodes + 1)
            seen.remove(nums[u])

        # Start traversal from the root (or as required by the directionality constraint)
        dfs(0, -1, set(), 0, 1)
        return [max_length, min_nodes]
# @lc code=end