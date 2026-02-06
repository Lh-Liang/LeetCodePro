#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum_modulus = 0
        mod_indices = defaultdict(list)
        mod_indices[0].append(-1) # To handle subarrays starting from index 0
        current_prefix_sum = 0
        distinct_subarrays = set()
        
        for i, num in enumerate(nums):
            current_prefix_sum += num
            prefix_sum_modulus = current_prefix_sum % k
            
            if prefix_sum_modulus in mod_indices:
                for start_index in mod_indices[prefix_sum_modulus]:
                    # Add tuple of subarray values as they represent distinct sequences of values.
                    distinct_subarrays.add(tuple(nums[start_index + 1:i + 1]))
            
            mod_indices[prefix_sum_modulus].append(i)
        
        return len(distinct_subarrays)
# @lc code=end