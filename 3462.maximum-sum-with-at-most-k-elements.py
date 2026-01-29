#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        all_candidates = []
        for i in range(len(grid)):
            # Only consider the row if the limit allows picking elements
            if limits[i] > 0:
                # Sort row descending to get the best candidates from this specific row
                row_sorted = sorted(grid[i], reverse=True)
                # Take the top 'limits[i]' elements
                all_candidates.extend(row_sorted[:limits[i]])
        
        # Sort all valid candidates globally
        all_candidates.sort(reverse=True)
        
        # The maximum sum of AT MOST k elements. Since all grid[i][j] >= 0, 
        # we take as many as possible up to k to maximize the sum.
        return sum(all_candidates[:k])
# @lc code=end