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
        
        def get_pos(i: int) -> int:
            x, y = points[i]
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 2 * side + (side - x)
            else:
                return 3 * side + (side - y)
        
        order = sorted(range(n), key=get_pos)
        
        def manh(i: int, j: int) -> int:
            xi, yi = points[i]
            xj, yj = points[j]
            return abs(xi - xj) + abs(yi - yj)
        
        def can(d: int) -> bool:
            if d * (k - 1) > 2 * side:
                return False
            
            selected = []
            
            def backtrack(start: int, cnt: int) -> bool:
                if cnt == k:
                    return True
                if n - start < k - cnt:
                    return False
                for cand in range(start, n):
                    orig = order[cand]
                    ok = True
                    for prev in selected:
                        if manh(prev, orig) < d:
                            ok = False
                            break
                    if ok:
                        selected.append(orig)
                        if backtrack(cand + 1, cnt + 1):
                            return True
                        selected.pop()
                return False
            
            return backtrack(0, 0)
        
        lo, hi = 0, 2 * side + 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

# @lc code=end