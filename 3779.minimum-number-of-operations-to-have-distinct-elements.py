#
# @lc app=leetcode id=3779 lang=python3
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Maximum index among first occurrences of duplicate pairs.
        max_dup_start = -1
        # Dictionary mapping value to its most recent occurrence index.
        last_occurrence = {}
        
        for idx, num in enumerate(nums):
            if num in last_occurrence:
                # Found a duplicate pair.
                # Update max_dup_start with the earlier occurrence index.
                max_dup_start = max(max_dup_start, last_occurrence[num])
            # Update the most recent occurrence.
            last_occurrence[num] = idx
        
        # Minimum start index needed.
        m = max_dup_start + 1
        # Number of operations required.
        return (m + 2) // 3
# @lc code=end