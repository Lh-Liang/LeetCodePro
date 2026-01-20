#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        # Iterate backwards to find the longest suffix with distinct elements
        # The suffix starts at index i
        valid_start_index = 0
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                valid_start_index = i + 1
                break
            seen.add(nums[i])
        
        # We need to remove elements from index 0 to valid_start_index - 1.
        # The count of elements to remove is exactly valid_start_index.
        # Each operation removes 3 elements.
        # Operations needed = ceil(valid_start_index / 3)
        return (valid_start_index + 2) // 3

# @lc code=end