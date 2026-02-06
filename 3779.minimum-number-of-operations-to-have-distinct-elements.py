#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        while len(nums) > len(set(nums)):
            # Remove up to three elements from start
            nums = nums[3:] if len(nums) >= 3 else []
            operations += 1
        return operations
# @lc code=end