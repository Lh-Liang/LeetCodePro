#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from itertools import combinations
        from collections import defaultdict
        
        def slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                return 'inf'  # Vertical line case
            return dy / dx  # Use division for slope calculation
        
        n = len(points)
        if n < 4:
            return 0
        
        trapezoid_count = 0
        checked_combinations = set()
        
        for quad in combinations(points, 4):
            quad_indices = tuple(sorted(quad))
            if quad_indices in checked_combinations:
                continue
            checked_combinations.add(quad_indices)
            slopes = defaultdict(int)
            pairs = list(combinations(quad, 2))
            for i in range(6):
                p1, p2 = pairs[i]
                m = slope(p1, p2)
                slopes[m] += 1
            if any(count >= 2 for count in slopes.values()):
                trapezoid_count += 1
        
        return trapezoid_count 
# @lc code=end