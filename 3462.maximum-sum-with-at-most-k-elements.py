#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        
        for row, limit in zip(grid, limits):
            # Sort the row in descending order
            sorted_row = sorted(row, reverse=True)
            # Take the top 'limit' elements from this row
            candidates.extend(sorted_row[:limit])
        
        # Sort all candidates in descending order
        candidates.sort(reverse=True)
        
        # Take the top k elements and return their sum
        return sum(candidates[:k])
# @lc code=end