#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
import sys
from typing import List

# Increase recursion depth for deep trees
sys.setrecursionlimit(10**5)

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # result[0] is max length, result[1] is min nodes
        result = [0, 1]
        
        # last_pos[val] stores the depth (index in current path) of the last occurrence of val
        last_pos = [-1] * (max(nums) + 1 if nums else 1)
        # path_dists[i] stores the distance from root to the i-th node in the current DFS path
        path_dists = []
        
        def dfs(u, p, current_dist, current_left):
            # Ancestor depth of the last occurrence of nums[u]
            old_pos = last_pos[nums[u]]
            
            # The special path ending at u must start at or after new_left
            # to ensure all values in the path are unique.
            new_left = current_left
            if old_pos + 1 > new_left:
                new_left = old_pos + 1
            
            # Current depth in the path (0-indexed)
            current_depth = len(path_dists)
            
            # Distance from root to the start node of this special path
            if new_left < current_depth:
                d_start = path_dists[new_left]
            else:
                d_start = current_dist
            
            path_len = current_dist - d_start
            num_nodes = current_depth - new_left + 1
            
            # Update the global best result
            if path_len > result[0]:
                result[0] = path_len
                result[1] = num_nodes
            elif path_len == result[0]:
                if num_nodes < result[1]:
                    result[1] = num_nodes
            
            # Prepare state for children
            last_pos[nums[u]] = current_depth
            path_dists.append(current_dist)
            
            for v, w in adj[u]:
                if v != p:
                    dfs(v, u, current_dist + w, new_left)
            
            # Backtrack: restore last_pos and path_dists for other branches
            path_dists.pop()
            last_pos[nums[u]] = old_pos

        # Start DFS from the root (node 0)
        dfs(0, -1, 0, 0)
        return result
# @lc code=end