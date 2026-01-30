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
            candidates.extend(sorted(row, reverse=True)[:limit])
        candidates.sort(reverse=True)
        return sum(candidates[:k])
# @lc code=end