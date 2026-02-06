#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from itertools import combinations
        def slope(p1, p2):
            if p1[0] == p2[0]: return float('inf') # Vertical line
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
        n = len(points)
        trapezoid_count = 0
        for quad in combinations(points, 4):
            p1, p2, p3, p4 = quad
            slopes = {slope(p1, p2), slope(p3, p4)} | {slope(p1, p3), slope(p2, p4)} | {slope(p1, p4), slope(p2, p3)}
            if len(slopes) < 6: # At least one pair of parallel sides means fewer than 6 unique slopes
                trapezoid_count += 1
        return trapezoid_count
# @lc code=end