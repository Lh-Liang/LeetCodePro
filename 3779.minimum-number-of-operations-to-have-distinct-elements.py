# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        operations = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]  # Remove first three elements
            operations += 1
        return operations # @lc code=end