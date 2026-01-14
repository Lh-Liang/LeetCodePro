#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter = 4 * side
        
        def point_to_pos(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y
        
        # Store (perimeter_position, x, y)
        coords = []
        for x, y in points:
            p = point_to_pos(x, y)
            coords.append((p, x, y))
        coords.sort()
        
        n = len(coords)
        
        # Double the array to handle cyclic nature
        doubled = coords + [(c[0] + perimeter, c[1], c[2]) for c in coords]
        
        def dist(i, j):
            return abs(doubled[i][1] - doubled[j][1]) + abs(doubled[i][2] - doubled[j][2])
        
        def check(d):
            for start in range(n):
                selected = [start]
                for _ in range(k - 1):
                    found = False
                    for idx in range(selected[-1] + 1, start + n):
                        ok = True
                        for s in selected:
                            if dist(idx, s) < d:
                                ok = False
                                break
                        if ok:
                            selected.append(idx)
                            found = True
                            break
                    if not found:
                        break
                if len(selected) == k:
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