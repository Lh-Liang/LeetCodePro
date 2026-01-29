#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # Pool to store the best candidates from each row
        all_candidates = []
        
        for i in range(len(grid)):
            # Extract the top 'limits[i]' elements from the current row
            # We sort the row in descending order to identify them
            row_sorted = sorted(grid[i], reverse=True)
            all_candidates.extend(row_sorted[:limits[i]])
        
        # Sort the global pool of candidates in descending order
        all_candidates.sort(reverse=True)
        
        # Sum the top 'k' elements from the pool
        # If k is 0, sum() returns 0 automatically
        return sum(all_candidates[:k])
# @lc code=end