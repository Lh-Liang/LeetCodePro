#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        start = 0
        used_operations = 0
        valid_count = 0

        for end in range(n):
            if end > 0 and nums[end] < nums[end - 1]:
                used_operations += nums[end - 1] - nums[end]
            while used_operations > k:
                if start < end and nums[start] > nums[start + 1]:
                    used_operations -= nums[start] - nums[start + 1]
                start += 1
            valid_count += (end - start + 1)
        return valid_count # @lc code=end