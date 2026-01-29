#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def get_perimeter_pos(p):
            x, y = p
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y

        # Sort points by perimeter position
        pts = sorted(points, key=get_perimeter_pos)
        n = len(pts)
        extended_pts = pts + pts

        def check(d):
            # next_idx[l] is the first index r > l s.t. Manhattan dist(pts[l], pts[r]) >= d
            next_idx = [0] * (2 * n)
            r = 0
            for l in range(2 * n):
                if r <= l: r = l + 1
                while r < 2 * n:
                    dist = abs(extended_pts[l][0] - extended_pts[r][0]) + abs(extended_pts[l][1] - extended_pts[r][1])
                    if dist >= d:
                        break
                    r += 1
                next_idx[l] = r

            # Optimization: If a solution exists, one starting point must be in the first 'gap'
            # This avoids checking all N starting points.
            limit = next_idx[0]
            for i in range(min(limit + 1, n)):
                curr = i
                for _ in range(k - 1):
                    curr = next_idx[curr]
                    if curr >= i + n:
                        break
                else:
                    # Check distance between last point and original starting point
                    if curr < i + n:
                        last_dist = abs(extended_pts[curr][0] - extended_pts[i][0]) + abs(extended_pts[curr][1] - extended_pts[i][1])
                        if last_dist >= d:
                            return True
            return False

        low, high = 0, 2 * side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid == 0 or check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
# @lc code=end