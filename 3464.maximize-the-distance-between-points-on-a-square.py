#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)
        
        def boundary_pos(p):
            x, y = p
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y
        
        pts = sorted(points, key=boundary_pos)
        
        def dist(i, j):
            return abs(pts[i % n][0] - pts[j % n][0]) + abs(pts[i % n][1] - pts[j % n][1])
        
        def check(d):
            for s in range(n):
                cur = s
                cnt = 1
                for nxt in range(s + 1, s + n):
                    if dist(cur, nxt) >= d:
                        cur = nxt
                        cnt += 1
                        if cnt == k:
                            break
                if cnt == k and dist(cur, s) >= d:
                    return True
            return False
        
        lo, hi = 1, 2 * side
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
# @lc code=end