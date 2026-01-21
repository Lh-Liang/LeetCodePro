#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        
        # Collect the top viable candidates from each row based on row limits
        for i in range(len(grid)):
            # Sort row in descending order to get largest elements first
            grid[i].sort(reverse=True)
            
            # Take at most limits[i] elements from this row
            # We only need to consider these because any element smaller than
            # the top limits[i] in this row would never be chosen over them
            # given the row constraint.
            candidates.extend(grid[i][:limits[i]])
            
        # Sort all gathered candidates in descending order
        candidates.sort(reverse=True)
        
        # Take the top k elements from the global pool
        return sum(candidates[:k])
        
# @lc code=end