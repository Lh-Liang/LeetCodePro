#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        # Sorting points based on x+y and x-y projections
        max_x_plus_y = max(x + y for x, y in points)
        min_x_plus_y = min(x + y for x, y in points)
        max_x_minus_y = max(x - y for x, y in points)
        min_x_minus_y = min(x - y for x, y in points)
        
        # The maximum possible partition factor is the largest difference between projections
        return max(max_x_plus_y - min_x_plus_y, max_x_minus_y - min_x_minus_y)
# @lc code=end