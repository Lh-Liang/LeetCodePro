# 
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Group all indices for each unique value in the array
        pos_map = defaultdict(list)
        for i, v in enumerate(nums):
            pos_map[v].append(i)
            
        # Precompute the minimum distance for every index in the array
        # Initialize with -1 for values that appear only once
        results = [-1] * n
        for v in pos_map:
            plist = pos_map[v]
            L = len(plist)
            if L > 1:
                for k in range(L):
                    curr_idx = plist[k]
                    # In a circular array, the closest equal element must be either
                    # the immediate predecessor or the immediate successor in the sorted index list.
                    
                    # Distance to the predecessor (moving counter-clockwise)
                    # Python's % operator handles negative results correctly for circularity
                    dist_left = (curr_idx - plist[k - 1]) % n
                    
                    # Distance to the successor (moving clockwise)
                    dist_right = (plist[(k + 1) % L] - curr_idx) % n
                    
                    # Store the minimum of the two possible directions
                    results[curr_idx] = min(dist_left, dist_right)
                    
        # Return the precomputed results for the requested indices
        return [results[q] for q in queries]
# @lc code=end