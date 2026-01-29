#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        while nums:
            if len(set(nums)) == len(nums):
                return operations
            if len(nums) <= 3:
                return operations + 1
            nums = nums[3:]
            operations += 1
        return operations
# @lc code=end