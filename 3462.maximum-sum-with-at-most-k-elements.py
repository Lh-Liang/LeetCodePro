#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # Create a list to store potential candidates for max sum
        candidates = []
        
        # Process each row to gather elements respecting individual limits
        for i, row in enumerate(grid):
            sorted_row = sorted(row, reverse=True)
            max_elements = min(limits[i], len(sorted_row))
            candidates.extend(sorted_row[:max_elements])
        
        # Use a heap to find the k largest elements from candidates
        if len(candidates) <= k:
            return sum(candidates)
        
        return sum(heapq.nlargest(k, candidates))
# @lc code=end