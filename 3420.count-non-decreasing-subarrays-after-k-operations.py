#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_count = 0
        start = 0
        current_ops = 0
        # Use two pointers to track valid subarrays
        for end in range(n):
            if end > 0 and nums[end] < nums[end - 1]:
                current_ops += nums[end - 1] - nums[end]
            while current_ops > k:
                if start < end and nums[start + 1] < nums[start]:
                    current_ops -= nums[start + 1] - nums[start]
                start += 1
            # Count all subarrays ending at 'end' starting from 'start'
            total_count += end - start + 1
        return total_count 
# @lc code=end