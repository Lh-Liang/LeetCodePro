#
# @lc app=leetcode id=3425 lang=python3
#
# [3425] Longest Special Path
#

# @lc code=start
import sys

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # Increase recursion limit to handle deep trees (N = 50,000)
        sys.setrecursionlimit(100000)
        
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # res[0]: max length, res[1]: min nodes for that length
        res = [0, 1]
        # last_pos[val] stores the depth of the most recent occurrence of 'val'
        # Constraint: 0 <= nums[i] <= 50,000
        last_pos = [-1] * 50001
        # dist_stack stores prefix sums of distances from root to node at depth i
        dist_stack = [0]
        
        def dfs(u, p, curr_dist, curr_depth, top_depth):
            old_pos = last_pos[nums[u]]
            # The special path ending at u cannot start at or above any previous 
            # occurrence of a value currently in the path.
            # top_depth tracks the 'highest' invalid depth.
            new_top_depth = max(top_depth, old_pos)
            
            # The valid unique path starts at depth (new_top_depth + 1)
            # Length = dist[curr_depth] - dist[new_top_depth + 1]
            # Nodes = curr_depth - new_top_depth
            path_len = curr_dist - dist_stack[new_top_depth + 1]
            num_nodes = curr_depth - new_top_depth
            
            if path_len > res[0]:
                res[0] = path_len
                res[1] = num_nodes
            elif path_len == res[0]:
                if num_nodes < res[1]:
                    res[1] = num_nodes
            
            # Update state for recursive calls
            last_pos[nums[u]] = curr_depth
            
            for v, w in adj[u]:
                if v != p:
                    dist_stack.append(curr_dist + w)
                    dfs(v, u, curr_dist + w, curr_depth + 1, new_top_depth)
                    dist_stack.pop()
            
            # Backtrack to restore state for other branches
            last_pos[nums[u]] = old_pos
            
        # Start DFS: node 0, no parent, distance 0, depth 0, top_depth -1
        dfs(0, -1, 0, 0, -1)
        return res
# @lc code=end