#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        seen_subarrays = set()
        start = 0
        current_sum = 0
        for end in range(len(nums)):
            current_sum += nums[end]
            while start <= end and current_sum % k == 0:
                seen_subarrays.add(tuple(nums[start:end+1]))
                current_sum -= nums[start]
                start += 1
            if current_sum % k == 0:
                seen_subarrays.add(tuple(nums[start:end+1]))
        return len(seen_subarrays)
# @lc code=end