#
# @lc app=leetcode id=3729 lang=python3
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        good_subarrays = set()
        for i in range(n):
            curr_sum = 0
            sub = []
            for j in range(i, n):
                curr_sum += nums[j]
                sub.append(nums[j])
                if curr_sum % k == 0:
                    good_subarrays.add(tuple(sub))
        return len(good_subarrays)
# @lc code=end