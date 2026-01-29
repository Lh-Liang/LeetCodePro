#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict
        def dfs(node, parent, path):
            max_length = 0
            min_nodes = float('inf') if len(path) > 1 else 1
            unique_values = set(path)
            for neighbor, length in adj[node]:
                if neighbor != parent:
                    next_path = path + [nums[neighbor]] if nums[neighbor] not in unique_values else path
                    if len(next_path) > len(path): # Check if it's still unique
                        child_length, child_nodes = dfs(neighbor, node, next_path)
                        total_length = child_length + length
                        max_length = max(max_length, total_length)
                        if total_length == max_length:
                            min_nodes = min(min_nodes, child_nodes + 1) # Include current node as well
            return max_length, min_nodes
        adj = defaultdict(list)
        for u, v, l in edges:
            adj[u].append((v,l))
            adj[v].append((u,l))
        result_length, result_nodes = dfs(0,-1,[nums[0]]) # Start DFS from root node 0 with its value in path
        return [result_length,result_nodes]
# @lc code=end