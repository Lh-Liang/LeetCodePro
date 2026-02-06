#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        left = 0
        needed_operations = 0
        for right in range(1, n):
            if nums[right] < nums[right - 1]:
                needed_operations += nums[right - 1] - nums[right]
            while needed_operations > k:
                if nums[left + 1] < nums[left]:
                    needed_operations -= nums[left] - nums[left + 1]
                left += 1
            result += right - left + 1
        return result
# @lc code=end