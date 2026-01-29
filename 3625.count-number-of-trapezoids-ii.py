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
        if n < 4:
            return 0
        
        def comb2(k: int) -> int:
            return k * (k - 1) // 2
        
        # Collect all unique slopes and pair counts
        slopes = set()
        slope_paircount = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                g = gcd(abs(dx), abs(dy))
                if g != 0:
                    dx //= g
                    dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                sl = (dy, dx)
                slopes.add(sl)
                slope_paircount[sl] += 1
        
        # Compute S
        S = 0
        for sl in slopes:
            if slope_paircount[sl] < 2:
                continue
            dy, dx = sl
            b_count = defaultdict(int)
            for x, y in points:
                b = dy * x - dx * y
                b_count[b] += 1
            sizes = [cnt for cnt in b_count.values() if cnt >= 2]
            m = len(sizes)
            for ii in range(m):
                for jj in range(ii + 1, m):
                    S += comb2(sizes[ii]) * comb2(sizes[jj])
        
        # Compute P: parallelograms via shared midpoints
        mid_to_diags = defaultdict(list)
        for i in range(n):
            for k in range(i + 1, n):
                sx = points[i][0] + points[k][0]
                sy = points[i][1] + points[k][1]
                mid_to_diags[(sx, sy)].append((i, k))
        
        P = 0
        for diags in mid_to_diags.values():
            ld = len(diags)
            for a in range(ld):
                for b in range(a + 1, ld):
                    i1, k1 = diags[a]
                    i2, k2 = diags[b]
                    ends = {i1, k1, i2, k2}
                    if len(ends) == 4:
                        P += 1
        
        return S - P

# @lc code=end