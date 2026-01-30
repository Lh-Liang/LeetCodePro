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
        # Helper to compute reduced slope between two points
        def get_slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx == 0: return ('inf', 0) # vertical
            sign = 1 if dx * dy >= 0 else -1
            dx, dy = abs(dx), abs(dy)
            g = gcd(dx, dy)
            return (sign * dy // g, dx // g)

        n = len(points)
        index_map = {tuple(points[i]): i for i in range(n)}
        slope_map = defaultdict(list)
        # Group all line segments by reduced slope
        for i in range(n):
            for j in range(i+1, n):
                slope = get_slope(points[i], points[j])
                slope_map[slope].append((i, j))

        # To avoid duplicates, store sorted tuple of indices
        trapezoids = set()
        for segs in slope_map.values():
            m = len(segs)
            for a in range(m):
                i1, j1 = segs[a]
                for b in range(a+1, m):
                    i2, j2 = segs[b]
                    idx = {i1, j1, i2, j2}
                    if len(idx) != 4: continue # must be 4 different points
                    quad = [points[i1], points[j1], points[i2], points[j2]]
                    # Check convexity: sort points in order, compute cross product
                    # We'll try all 24 orderings (could optimize further but n is small)
                    from itertools import permutations
                    for order in permutations([i1, j1, i2, j2]):
                        xys = [points[k] for k in order]
                        # Check if it is convex
                        cp = []
                        valid = True
                        for k in range(4):
                            dx1 = xys[(k+1)%4][0] - xys[k][0]
                            dy1 = xys[(k+1)%4][1] - xys[k][1]
                            dx2 = xys[(k+2)%4][0] - xys[(k+1)%4][0]
                            dy2 = xys[(k+2)%4][1] - xys[(k+1)%4][1]
                            cross = dx1*dy2 - dy1*dx2
                            cp.append(cross)
                        if all(c > 0 for c in cp) or all(c < 0 for c in cp):
                            # Convex
                            # To avoid duplicates, always store the sorted tuple
                            trapezoids.add(tuple(sorted([i1, j1, i2, j2])))
                            break
        return len(trapezoids)
# @lc code=end