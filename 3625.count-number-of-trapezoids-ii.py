#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
from collections import defaultdict
import math

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
            
        def get_slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                return (0, 1)
            if dy == 0:
                return (1, 0)
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0 and dy < 0:
                dy = -dy
            return (dx, dy)

        # slope_groups[slope][line_constant] = count_of_pairs_on_this_line
        # A line is defined by its slope (dx, dy) and the constant C = dy*x - dx*y
        slope_groups = defaultdict(lambda: defaultdict(int))
        midpoints = defaultdict(int)
        collinear_midpoints = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                slope = get_slope(p1, p2)
                dx, dy = slope
                # Line equation: dy*x - dx*y = C
                c = dy * p1[0] - dx * p1[1]
                slope_groups[slope][c] += 1
                
                # For parallelogram counting
                mx, my = p1[0] + p2[0], p1[1] + p2[1]
                midpoints[(mx, my)] += 1
                collinear_midpoints[(slope, c)][(mx, my)] += 1

        total_trapezoids = 0
        for slope in slope_groups:
            lines = list(slope_groups[slope].values())
            if len(lines) < 2:
                continue
            
            sum_segments = sum(lines)
            sum_sq_segments = sum(x*x for x in lines)
            # Number of ways to pick two segments from different lines of the same slope
            total_trapezoids += (sum_segments**2 - sum_sq_segments) // 2

        parallelograms = 0
        for m in midpoints:
            cnt = midpoints[m]
            if cnt >= 2:
                parallelograms += cnt * (cnt - 1) // 2
        
        # Subtract collinear midpoints (4 points on the same line cannot form a trapezoid/parallelogram)
        for line_key in collinear_midpoints:
            for m in collinear_midpoints[line_key]:
                cnt = collinear_midpoints[line_key][m]
                if cnt >= 2:
                    parallelograms -= cnt * (cnt - 1) // 2

        # Each parallelogram has 2 pairs of parallel sides, so it was counted twice in total_trapezoids.
        # To count each unique parallelogram once, we subtract it once.
        return total_trapezoids - parallelograms
# @lc code=end