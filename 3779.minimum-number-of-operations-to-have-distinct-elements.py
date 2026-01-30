#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        # Step 1: Early check for empty or all-distinct array
        if len(nums) == 0 or len(set(nums)) == len(nums):
            return 0
        while True:
            # Remove first three elements (or all remaining if less than three)
            nums = nums[3:]
            ops += 1
            # Check stopping condition
            if len(nums) == 0 or len(set(nums)) == len(nums):
                return ops
# @lc code=end