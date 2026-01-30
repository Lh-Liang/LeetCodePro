#
# @lc app=leetcode id=3434 lang=python3
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        max_freq = 0
        for right in range(len(nums)):
            total += nums[right]
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
        return max_freq
# @lc code=end