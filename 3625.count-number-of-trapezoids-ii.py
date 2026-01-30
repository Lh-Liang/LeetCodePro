#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slope_map = defaultdict(list)
        # For every pair of points, compute the slope and store the segment
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0:
                    slope = (1, 0)
                elif dy == 0:
                    slope = (0, 1)
                else:
                    g = gcd(dy, dx)
                    slope = (dy // g, dx // g)
                slope_map[slope].append((i, j))

        unique_quads = set()
        # For each slope, collect candidate pairs of disjoint segments
        for segs in slope_map.values():
            m = len(segs)
            for i in range(m):
                a1, a2 = segs[i]
                for j in range(i+1, m):
                    b1, b2 = segs[j]
                    quad_indices = {a1, a2, b1, b2}
                    if len(quad_indices) != 4:
                        continue
                    quad = tuple(sorted(quad_indices))
                    if quad in unique_quads:
                        continue
                    # Efficient convexity check for quadrilaterals
                    pts = [points[q] for q in quad]
                    xs, ys = zip(*pts)
                    # Check all 3-point combinations for collinearity
                    collinear = False
                    for i1 in range(4):
                        x0, y0 = pts[i1]
                        x1, y1 = pts[(i1 + 1) % 4]
                        x2, y2 = pts[(i1 + 2) % 4]
                        if (y1 - y0)*(x2 - x0) == (y2 - y0)*(x1 - x0):
                            collinear = True
                            break
                    if collinear:
                        continue
                    unique_quads.add(quad)
        return len(unique_quads)
# @lc code=end