#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # Group indices by value
        value_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            value_to_indices[num].append(i)
        
        # Precompute the minimum distance for each index
        min_dist = [-1] * n
        
        for indices in value_to_indices.values():
            if len(indices) < 2:
                continue
            
            m = len(indices)
            for i in range(m):
                curr = indices[i]
                prev = indices[(i - 1) % m]
                next_idx = indices[(i + 1) % m]
                
                # Distance to previous and next index (circular)
                dist_prev = min(abs(curr - prev), n - abs(curr - prev))
                dist_next = min(abs(curr - next_idx), n - abs(curr - next_idx))
                
                min_dist[curr] = min(dist_prev, dist_next)
        
        return [min_dist[q] for q in queries]
# @lc code=end