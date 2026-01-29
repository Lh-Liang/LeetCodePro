#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
import sys
from typing import List

# Increase recursion depth for deep trees
sys.setrecursionlimit(100000)

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return [0, 0]
        
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # Primary metric: max_len, Secondary metric: min_nodes
        self.max_len = -1
        self.min_nodes = float('inf')
        
        # last_pos[val] = depth of the last occurrence of 'val' in current path
        # Initialize with -1 to indicate the value hasn't been seen yet.
        last_pos = [-1] * 50001
        # prefix_dists[d] = sum of edge weights from root to node at depth d
        prefix_dists = [0]
        
        def dfs(u, p, current_dist, top_depth):
            val = nums[u]
            curr_depth = len(prefix_dists) - 1
            
            # Update the starting boundary of the valid unique-value path
            # It must be below the last occurrence of the current value
            old_val_pos = last_pos[val]
            new_top_depth = max(top_depth, old_val_pos + 1)
            
            # Calculate length and node count for the special path ending at node u
            length = current_dist - prefix_dists[new_top_depth]
            num_nodes = curr_depth - new_top_depth + 1
            
            # Update global bests
            if length > self.max_len:
                self.max_len = length
                self.min_nodes = num_nodes
            elif length == self.max_len:
                if num_nodes < self.min_nodes:
                    self.min_nodes = num_nodes
            
            # Save current state for backtracking
            last_pos[val] = curr_depth
            
            for v, w in adj[u]:
                if v != p:
                    prefix_dists.append(current_dist + w)
                    dfs(v, u, current_dist + w, new_top_depth)
                    prefix_dists.pop()
            
            # Restore state for sibling branches
            last_pos[val] = old_val_pos
            
        dfs(0, -1, 0, 0)
        
        return [self.max_len, int(self.min_nodes)]
# @lc code=end