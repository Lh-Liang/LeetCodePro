#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        s = side
        n = len(points)

        def perim_t(x: int, y: int) -> int:
            # (0,0) -> (s,0) -> (s,s) -> (0,s) -> (0,0)
            if y == 0:
                return x
            if x == s:
                return s + y
            if y == s:
                return 3 * s - x
            # x == 0
            return 4 * s - y

        pts = [(perim_t(x, y), x, y) for x, y in points]
        pts.sort()
        xs = [x for _, x, _ in pts]
        ys = [y for _, _, y in pts]

        # Build tripled arrays for safe indexing up to i+n (with i < 2n).
        xs3 = xs + xs + xs
        ys3 = ys + ys + ys

        def manhattan(i: int, j: int) -> int:
            return abs(xs3[i] - xs3[j]) + abs(ys3[i] - ys3[j])

        def feasible_small(D: int) -> bool:
            # D <= side
            if D <= 0:
                return True
            if k == 1:
                return True
            # nxt only needed for i in [0, 2n)
            nxt = [0] * (2 * n)
            for i in range(2 * n):
                lo = i + 1
                hi = i + n + 1  # exclusive
                # Find first j in [i+1, i+n] with dist(i,j) >= D.
                while lo < hi:
                    mid = (lo + hi) // 2
                    if manhattan(i, mid) >= D:
                        hi = mid
                    else:
                        lo = mid + 1
                nxt[i] = lo  # may be i+n+1 (meaning not found within one lap)

            for start in range(n):
                idx = start
                limit = start + n
                ok = True
                for _ in range(k - 1):
                    idx = nxt[idx]
                    if idx >= limit:
                        ok = False
                        break
                if not ok:
                    continue
                if manhattan(start, idx) >= D:
                    return True
            return False

        def get_min_max_in_range(arr: List[int], lo: int, hi: int):
            # returns (min_val, max_val) within [lo, hi], or (None, None) if empty
            L = bisect.bisect_left(arr, lo)
            R = bisect.bisect_right(arr, hi) - 1
            if L <= R:
                return arr[L], arr[R]
            return None, None

        def feasible_large(D: int) -> bool:
            # D > side, only possible if k == 4
            if k != 4:
                return False
            if D <= s:
                return feasible_small(D)

            d1 = D - s  # > 0

            # Collect non-corner points from each edge
            B = []  # bottom: y=0, store x
            T = []  # top: y=s, store x
            L = []  # left: x=0, store y
            R = []  # right: x=s, store y

            for x, y in points:
                if x == 0 and y == 0:
                    continue
                if x == 0 and y == s:
                    continue
                if x == s and y == 0:
                    continue
                if x == s and y == s:
                    continue
                if y == 0:
                    B.append(x)
                elif x == s:
                    R.append(y)
                elif y == s:
                    T.append(x)
                else:  # x == 0
                    L.append(y)

            if not B or not T or not L or not R:
                return False

            B.sort(); T.sort(); L.sort(); R.sort()

            # For each xB, determine feasible xT region from adjacent constraints and opposite constraint.
            for xB in B:
                # From non-empty yL interval:
                # D - xB <= s + xT - D  => xT >= 2D - s - xB
                # From non-empty yR interval:
                # D - s + xB <= 2s - xT - D => xT <= 3s - 2D + xB
                base_lo = max(0, 2 * D - s - xB)
                base_hi = min(s, 3 * s - 2 * D + xB)
                if base_lo > base_hi:
                    continue

                # Apply opposite constraint |xT - xB| >= d1
                i1_lo, i1_hi = base_lo, min(base_hi, xB - d1)
                i2_lo, i2_hi = max(base_lo, xB + d1), base_hi

                # Find minimum feasible xT from union
                candidates = []
                if i1_lo <= i1_hi:
                    pos = bisect.bisect_left(T, i1_lo)
                    if pos < len(T) and T[pos] <= i1_hi:
                        candidates.append(T[pos])
                if i2_lo <= i2_hi:
                    pos = bisect.bisect_left(T, i2_lo)
                    if pos < len(T) and T[pos] <= i2_hi:
                        candidates.append(T[pos])

                # Find maximum feasible xT from union
                if i2_lo <= i2_hi:
                    pos = bisect.bisect_right(T, i2_hi) - 1
                    if pos >= 0 and T[pos] >= i2_lo:
                        candidates.append(T[pos])
                if i1_lo <= i1_hi:
                    pos = bisect.bisect_right(T, i1_hi) - 1
                    if pos >= 0 and T[pos] >= i1_lo:
                        candidates.append(T[pos])

                if not candidates:
                    continue

                # Test unique candidates
                for xT in set(candidates):
                    if abs(xB - xT) < d1:
                        continue

                    # yL interval
                    yL_lo = D - xB
                    yL_hi = s + xT - D
                    if yL_lo > yL_hi:
                        continue

                    # yR interval
                    yR_lo = D - s + xB
                    yR_hi = 2 * s - xT - D
                    if yR_lo > yR_hi:
                        continue

                    minL, maxL = get_min_max_in_range(L, yL_lo, yL_hi)
                    if minL is None:
                        continue
                    minR, maxR = get_min_max_in_range(R, yR_lo, yR_hi)
                    if minR is None:
                        continue

                    # Need |yL - yR| >= d1. It is achievable iff extremes can separate enough.
                    if maxL - minR >= d1 or maxR - minL >= d1:
                        return True

            return False

        def feasible(D: int) -> bool:
            if D <= s:
                return feasible_small(D)
            return feasible_large(D)

        hi = 2 * s if k == 4 else s
        lo = 0
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

# @lc code=end
