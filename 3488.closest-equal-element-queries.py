#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Map each value to a sorted list of indices where it occurs
        pos_map = defaultdict(list)
        for i, val in enumerate(nums):
            pos_map[val].append(i)
            
        # Map each index to its position within its value's sorted list
        idx_to_pos_in_list = [0] * len(nums)
        for val, indices in pos_map.items():
            for pos, original_idx in enumerate(indices):
                idx_to_pos_in_list[original_idx] = pos
                
        n = len(nums)
        results = []
        
        for q_idx in queries:
            val = nums[q_idx]
            indices = pos_map[val]
            m = len(indices)
            
            if m == 1:
                results.append(-1)
                continue
            
            # Position of the query index in the sorted list of indices
            k = idx_to_pos_in_list[q_idx]
            
            # Neighbor to the left (circularly)
            left_neighbor = indices[(k - 1) % m]
            # Neighbor to the right (circularly)
            right_neighbor = indices[(k + 1) % m]
            
            # Calculate circular distances
            dist_left = (q_idx - left_neighbor) % n
            dist_right = (right_neighbor - q_idx) % n
            
            results.append(min(dist_left, dist_right))
            
        return results
# @lc code=end