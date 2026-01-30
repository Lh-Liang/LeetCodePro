#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        j = 0
        cost = 0
        for i in range(n):
            # Expand right pointer j as much as possible
            while j < n:
                if j > i and nums[j-1] > nums[j]:
                    cost += nums[j-1] - nums[j]
                if cost > k:
                    if j > i and nums[j-1] > nums[j]:
                        cost -= nums[j-1] - nums[j]
                    break
                j += 1
            res += j - i
            if i + 1 < n and nums[i] > nums[i+1]:
                cost -= nums[i] - nums[i+1]
        return res
# @lc code=end