#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # Build tree adjacency list
        n = len(nums)
        tree = [[] for _ in range(n)]
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))

        best_length = 0
        min_nodes = float('inf')
        from collections import defaultdict
        
        def dfs(node, parent, seen, used_dup, curr_length, curr_nodes):
            nonlocal best_length, min_nodes
            val = nums[node]
            is_dup = val in seen
            if is_dup and used_dup:
                return
            if curr_length > best_length:
                best_length = curr_length
                min_nodes = curr_nodes
            elif curr_length == best_length and curr_nodes < min_nodes:
                min_nodes = curr_nodes
            # Visit children
            if not is_dup:
                seen.add(val)
            for neighbor, w in tree[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node, seen, used_dup or is_dup, curr_length + w, curr_nodes + 1)
            if not is_dup:
                seen.remove(val)

        # Use only a single traversal from the root to ensure efficiency and correct directionality
        dfs(0, -1, set(), False, 0, 1)
        return [best_length, min_nodes]
# @lc code=end