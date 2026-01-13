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
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]

        def norm_dir(dx: int, dy: int):
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            return dx, dy

        # 1) Group all segments by slope, store (i, j, c) where c identifies the supporting line
        # for this slope via a*x + b*y = c, with (a,b) being the canonical normal to the slope.
        slope_segs = defaultdict(list)  # (dx,dy) -> list[(i,j,c)]

        for i in range(n):
            xi, yi = xs[i], ys[i]
            for j in range(i + 1, n):
                dx0 = xs[j] - xi
                dy0 = ys[j] - yi
                dx, dy = norm_dir(dx0, dy0)

                # Normal vector to direction (dx,dy) is (dy,-dx). Canonicalize sign.
                a, b = dy, -dx
                if a < 0 or (a == 0 and b < 0):
                    a, b = -a, -b
                c = a * xi + b * yi

                slope_segs[(dx, dy)].append((i, j, c))

        def comb2(x: int) -> int:
            return x * (x - 1) // 2

        # 2) Count trapezoids via parallel opposite sides
        total_parallel_pairs = 0
        for segs in slope_segs.values():
            k = len(segs)
            if k < 2:
                continue

            total_pairs = comb2(k)

            # pairs sharing an endpoint
            deg_point = defaultdict(int)

            # line counts and (line,point) endpoint degrees within that line
            line_seg = defaultdict(int)          # c -> count of segments on that line
            line_point_deg = defaultdict(int)    # (c, point) -> count

            for i, j, c in segs:
                deg_point[i] += 1
                deg_point[j] += 1

                line_seg[c] += 1
                line_point_deg[(c, i)] += 1
                line_point_deg[(c, j)] += 1

            shared_endpoint_pairs = sum(comb2(v) for v in deg_point.values())

            # disjoint collinear pairs (segments on same line with no shared endpoints)
            line_shared = defaultdict(int)  # c -> sum over points on that line of C(deg,2)
            for (c, _p), v in line_point_deg.items():
                if v >= 2:
                    line_shared[c] += comb2(v)

            disjoint_collinear_pairs = 0
            for c, t in line_seg.items():
                col_pairs = comb2(t)
                disjoint_collinear_pairs += col_pairs - line_shared.get(c, 0)

            valid = total_pairs - shared_endpoint_pairs - disjoint_collinear_pairs
            total_parallel_pairs += valid

        # 3) Count (non-degenerate) parallelograms to fix double counting
        mid_total = defaultdict(int)     # (mx,my) -> total diagonals with this midpoint
        diag_count = defaultdict(int)    # (mx,my,dx,dy) -> count of diagonals with this midpoint and slope

        for i in range(n):
            xi, yi = xs[i], ys[i]
            for j in range(i + 1, n):
                mx = xi + xs[j]
                my = yi + ys[j]
                mid_total[(mx, my)] += 1

                dx0 = xs[j] - xi
                dy0 = ys[j] - yi
                dx, dy = norm_dir(dx0, dy0)
                diag_count[(mx, my, dx, dy)] += 1

        mid_collinear_pairs = defaultdict(int)  # (mx,my) -> sum over slopes of C(cnt,2)
        for key, cnt in diag_count.items():
            if cnt >= 2:
                mx, my, _dx, _dy = key
                mid_collinear_pairs[(mx, my)] += comb2(cnt)

        parallelograms = 0
        for mid, t in mid_total.items():
            if t >= 2:
                parallelograms += comb2(t) - mid_collinear_pairs.get(mid, 0)

        return total_parallel_pairs - parallelograms

# @lc code=end
