#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        
        # For each row, pick the largest allowed elements based on limits[i]
        for i in range(len(grid)):
            # Sort the row in descending order to easily pick the largest ones
            grid[i].sort(reverse=True)
            
            # Take up to limits[i] elements from this row
            # We extend the candidates list with these top elements
            candidates.extend(grid[i][:limits[i]])
        
        # Now we have a list of all possible candidates that satisfy row constraints.
        # To maximize the total sum with at most k elements, we pick the largest k 
        # from this combined pool.
        candidates.sort(reverse=True)
        
        return sum(candidates[:k])

# @lc code=end