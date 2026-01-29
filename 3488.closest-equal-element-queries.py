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
        val_to_indices = defaultdict(list)
        # pos_in_list stores the index of nums[i] within the list val_to_indices[nums[i]]
        pos_in_list = [0] * n
        
        for i, val in enumerate(nums):
            pos_in_list[i] = len(val_to_indices[val])
            val_to_indices[val].append(i)
            
        ans = []
        for q_idx in queries:
            val = nums[q_idx]
            indices = val_to_indices[val]
            k = len(indices)
            
            if k == 1:
                ans.append(-1)
                continue
            
            p = pos_in_list[q_idx]
            
            # The closest elements in a circular array are the adjacent ones in the sorted index list
            prev_idx = indices[(p - 1) % k]
            next_idx = indices[(p + 1) % k]
            
            # Calculate circular distances using modulo to handle wraparound correctly
            dist_prev = (q_idx - prev_idx) % n
            dist_next = (next_idx - q_idx) % n
            
            ans.append(min(dist_prev, dist_next))
            
        return ans
# @lc code=end