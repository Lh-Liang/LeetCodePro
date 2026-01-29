#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for i in range(len(grid)):
            # Sort row descending and take the top 'limits[i]' elements
            row_sorted = sorted(grid[i], reverse=True)
            candidates.extend(row_sorted[:limits[i]])
        
        # Sort all row-wise candidates globally and pick the top k
        candidates.sort(reverse=True)
        return sum(candidates[:k])
# @lc code=end