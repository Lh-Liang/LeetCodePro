#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
import math
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slopes = defaultdict(lambda: defaultdict(int))
        
        def get_slope_and_line(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0:
                return (0, 1), p1[0]
            if dy == 0:
                return (1, 0), p1[1]
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            # Line equation: dy*x - dx*y = c
            c = dy * p1[0] - dx * p1[1]
            return (dx, dy), c

        for i in range(n):
            for j in range(i + 1, n):
                slope, line = get_slope_and_line(points[i], points[j])
                slopes[slope][line] += 1
        
        total_p_s = 0
        for slope in slopes:
            line_counts = list(slopes[slope].values())
            sum_counts = sum(line_counts)
            sum_sq_counts = sum(x * x for x in line_counts)
            # Pairs of segments with same slope on different lines
            total_p_s += (sum_counts**2 - sum_sq_counts) // 2
            
        midpoints = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            for j in range(i + 1, n):
                mx = points[i][0] + points[j][0]
                my = points[i][1] + points[j][1]
                slope, _ = get_slope_and_line(points[i], points[j])
                midpoints[(mx, my)][slope] += 1
        
        total_parallelograms = 0
        for m_coord in midpoints:
            m_slopes = list(midpoints[m_coord].values())
            m_sum = sum(m_slopes)
            m_sum_sq = sum(x * x for x in m_slopes)
            # Parallelograms with this midpoint: pairs of segments with different slopes
            total_parallelograms += (m_sum**2 - m_sum_sq) // 2
            
        return total_p_s - total_parallelograms
# @lc code=end