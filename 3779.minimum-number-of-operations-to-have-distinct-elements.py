#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                break
            nums = nums[3:] if len(nums) >= 3 else []
            ops += 1
        return ops
# @lc code=end