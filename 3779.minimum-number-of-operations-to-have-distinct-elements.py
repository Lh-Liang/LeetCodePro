#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        # Find the longest suffix that has distinct elements
        # We iterate backwards from the end of the array
        last_duplicate_idx = -1
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                last_duplicate_idx = i
                break
            seen.add(nums[i])
        
        if last_duplicate_idx == -1:
            return 0
            
        # Number of elements that MUST be removed
        elements_to_remove = last_duplicate_idx + 1
        
        # Each operation removes 3 elements
        # Using ceiling division: (a + b - 1) // b
        return (elements_to_remove + 2) // 3
# @lc code=end