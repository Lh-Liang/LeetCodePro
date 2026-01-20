#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
import sys

# Increase recursion depth to handle deep trees as N can be up to 50,000
sys.setrecursionlimit(100000)

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Helper function for DFS
        # Returns a tuple of two lists: (max_sums, min_sums)
        # max_sums[j] stores the max subtree sum given distance to nearest inverted ancestor is j
        # min_sums[j] stores the min subtree sum given distance to nearest inverted ancestor is j
        # Indices are 1-based for convenience (0 is unused)
        def dfs(u, p):
            # Collect results from children first
            children_results = []
            for v in adj[u]:
                if v != p:
                    children_results.append(dfs(v, u))
            
            # Current node's value
            val = nums[u]
            
            # Arrays to store results for states 1 to k
            # Initialize with 0, but we will overwrite 1..k
            curr_maxs = [0] * (k + 1)
            curr_mins = [0] * (k + 1)
            
            # 1. Fill states where we CANNOT invert u (distance j < k)
            # If dist to ancestor is j, child will be at distance j+1
            # We iterate j from 1 to k-1
            for j in range(1, k):
                s_max = val
                s_min = val
                next_dist = j + 1
                # Sum up contributions from all children
                for c_maxs, c_mins in children_results:
                    s_max += c_maxs[next_dist]
                    s_min += c_mins[next_dist]
                curr_maxs[j] = s_max
                curr_mins[j] = s_min
            
            # 2. Fill state where we CAN invert u (distance j == k)
            # Option A: Don't invert u. Child sees distance k (capped at k).
            no_inv_max = val
            no_inv_min = val
            for c_maxs, c_mins in children_results:
                no_inv_max += c_maxs[k]
                no_inv_min += c_mins[k]
            
            # Option B: Invert u. Child sees distance 1.
            # If we invert, the values in subtree flip.
            # Total sum = - ( val + sum(children_sums_at_dist_1) )
            # To maximize total, we need to minimize the inner sum.
            # To minimize total, we need to maximize the inner sum.
            inv_max = -val
            inv_min = -val
            for c_maxs, c_mins in children_results:
                # maximize -> - (min of child)
                inv_max += -c_mins[1]
                # minimize -> - (max of child)
                inv_min += -c_maxs[1]
            
            curr_maxs[k] = max(no_inv_max, inv_max)
            curr_mins[k] = min(no_inv_min, inv_min)
            
            return curr_maxs, curr_mins

        # Root is effectively at distance infinity >= k from any inverted ancestor
        root_maxs, _ = dfs(0, -1)
        
        return root_maxs[k]

# @lc code=end