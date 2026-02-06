#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # Flatten list of potential selections according to limits
        candidates = []
        for i in range(len(grid)):
            # Sort each row in descending order
            sorted_row = sorted(grid[i], reverse=True)
            # Take only up to limits[i] from each row
            candidates.extend(sorted_row[:limits[i]])
        # Sort all candidates in descending order to pick top 'k'
        candidates.sort(reverse=True)
        # Sum up to 'k' largest numbers among candidates
        return sum(candidates[:k])
# @lc code=end