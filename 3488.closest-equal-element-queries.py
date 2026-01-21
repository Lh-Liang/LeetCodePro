#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
import collections
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        val_to_indices = collections.defaultdict(list)
        
        # Group indices for each value. 
        # Since we iterate from 0 to n-1, lists will be sorted.
        for i, v in enumerate(nums):
            val_to_indices[v].append(i)
        
        # Precompute the minimum distance for every index
        min_dist = [-1] * n
        for indices in val_to_indices.values():
            k = len(indices)
            if k < 2:
                continue
            
            for i in range(k):
                curr_idx = indices[i]
                # Distance to the next neighbor in clockwise direction
                # Python's modulo operator handles negative results correctly
                d_next = (indices[(i + 1) % k] - curr_idx) % n
                # Distance to the previous neighbor in counter-clockwise direction
                # (which is the clockwise distance from the previous to current)
                d_prev = (curr_idx - indices[i - 1]) % n
                
                min_dist[curr_idx] = min(d_next, d_prev)
        
        # Answer each query using the precomputed results
        return [min_dist[q] for q in queries]

# @lc code=end