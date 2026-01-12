#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
from typing import List
from collections import defaultdict
import math

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        
        # Group pairs by slope and then by line constant c
        # slope = (dy, dx) reduced, c = x*dy - y*dx
        slope_groups = defaultdict(lambda: defaultdict(int))
        # Group pairs by midpoint to count parallelograms
        midpoint_groups = defaultdict(int)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                # Midpoint calculation (scaled by 2 to keep integers)
                mx, my = x1 + x2, y1 + y2
                midpoint_groups[(mx, my)] += 1
                
                # Slope calculation
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    if dx < 0:
                        dx, dy = -dx, -dy
                    common = math.gcd(dx, dy)
                    dx //= common
                    dy //= common
                
                # c = x*dy - y*dx is the constant for the line equation dy*X - dx*Y = c
                c = x1 * dy - y1 * dx
                slope_groups[(dy, dx)][c] += 1
                
        total_parallel_pairs = 0
        for slope in slope_groups:
            counts = list(slope_groups[slope].values())
            total_slope_segments = sum(counts)
            # Calculate pairs of segments with same slope on different lines
            # Sum_{i < j} counts[i] * counts[j]
            sum_sq = sum(c * c for c in counts)
            total_parallel_pairs += (total_slope_segments**2 - sum_sq) // 2
            
        parallelogram_count = 0
        for count in midpoint_groups.values():
            if count >= 2:
                parallelogram_count += (count * (count - 1)) // 2
                
        # Unique Trapezoids = (Pairs of Parallel Segments) - (Parallelograms)
        return total_parallel_pairs - parallelogram_count
# @lc code=end