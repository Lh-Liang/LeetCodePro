#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

from typing import List
from math import gcd, comb
from collections import defaultdict

# @lc code=start
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        point_set = set(tuple(p) for p in points)

        # Count parallelograms using vector construction
        para_count = 0
        for i in range(n):
            xa, ya = points[i]
            for j in range(n):
                if j == i:
                    continue
                xb, yb = points[j]
                vx = xb - xa
                vy = yb - ya
                for k in range(n):
                    if k == i or k == j:
                        continue
                    xc, yc = points[k]
                    wx = xc - xa
                    wy = yc - ya
                    xd = xb + xc - xa
                    yd = yb + yc - ya
                    pt_d = (xd, yd)
                    if (pt_d in point_set and
                        pt_d != (xa, ya) and
                        pt_d != (xb, yb) and
                        pt_d != (xc, yc)):
                        cross = vx * wy - vy * wx
                        if cross != 0:
                            para_count += 1
        num_para = para_count // 8

        # Get all unique slopes
        slopes = set()
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slopes.add((dx, dy))

        # For each slope, group points by line (b), compute contributions
        total = 0
        for dx, dy in slopes:
            line_to_count = defaultdict(int)
            for p in points:
                x, y = p
                b = dy * x - dx * y
                line_to_count[b] += 1
            sizes = [cnt for cnt in line_to_count.values() if cnt >= 2]
            m = len(sizes)
            for p in range(m):
                for q in range(p + 1, m):
                    total += comb(sizes[p], 2) * comb(sizes[q], 2)

        return total - num_para

# @lc code=end
