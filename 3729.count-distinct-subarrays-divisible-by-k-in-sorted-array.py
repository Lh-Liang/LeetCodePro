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
        prefix_sum = 0
        mod_count = defaultdict(int)
        mod_count[0] = 1  # Base case for mod zero indicating a complete subarray is divisible by k.
        result_set = set()
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            current_mod = prefix_sum % k
            # Handle negative mods if necessary (not likely due to constraints but good practice)
            if current_mod < 0:
                current_mod += k
            
            # Check previous occurrences of this mod value to find valid subarrays ending here.
            if current_mod in mod_count:
                # Only check and add new subarray sequences that are unique based on the subarray itself.
                result_set.add(tuple(nums[j] for j in range(i - mod_count[current_mod] + 1, i + 1)))
            
            # Update or initialize this mod count.
            mod_count[current_mod] += 1
        
        return len(result_set)
# @lc code=end