#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
import sys
from typing import List

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # Increase recursion limit for potentially deep trees
        sys.setrecursionlimit(200000)
        
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # res[0] = max_length, res[1] = min_nodes
        # Initialize max_length to 0 and min_nodes to 1 (single node path)
        res = [0, 1]
        
        # last_pos[val] stores the depth of the most recent node with value 'val' in current path
        last_pos = [-1] * 50001
        # path_distances[d] stores the distance from root to the node at depth d
        path_distances = [0] * (n + 1)
        
        def dfs(u, p, current_dist, depth, current_L):
            # The window start L must be after the last seen position of the current node's value
            # to ensure all values in the path [new_L, depth] are unique.
            new_L = max(current_L, last_pos[nums[u]] + 1)
            
            path_distances[depth] = current_dist
            
            # Calculate length and node count for the special path ending at u
            length = current_dist - path_distances[new_L]
            nodes = depth - new_L + 1
            
            if length > res[0]:
                res[0] = length
                res[1] = nodes
            elif length == res[0]:
                if nodes < res[1]:
                    res[1] = nodes
            
            # Save current last_pos to backtrack later
            old_pos = last_pos[nums[u]]
            last_pos[nums[u]] = depth
            
            for v, w in adj[u]:
                if v != p:
                    dfs(v, u, current_dist + w, depth + 1, new_L)
            
            # Backtrack to restore the state for other branches
            last_pos[nums[u]] = old_pos

        dfs(0, -1, 0, 0, 0)
        
        return res
# @lc code=end