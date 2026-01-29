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
            # Check if it's feasible to turn entire window into nums[right]
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            # Update maximum frequency found so far.
            max_freq = max(max_freq, right - left + 1)
        return max_freq
# @lc code=end