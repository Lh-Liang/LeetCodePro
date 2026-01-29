#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        ops_needed = 0
        left = 0
        for right in range(n):
            if right > 0 and nums[right] < nums[right - 1]:
                ops_needed += nums[right - 1] - nums[right]
            while ops_needed > k:
                if left < right and nums[left + 1] < nums[left]:
                    ops_needed -= nums[left + 1] - nums[left]
                left += 1
            count += right - left + 1
        return count
# @lc code=end