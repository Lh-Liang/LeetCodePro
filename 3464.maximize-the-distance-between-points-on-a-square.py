#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def get_pos(p):
            x, y = p
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y

        def get_md(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        pts = sorted([(get_pos(p), p) for p in points])
        n = len(pts)
        perimeter = 4 * side

        def check(d):
            # If a solution exists, at least one point must be in the first 1/k of the perimeter
            # or specifically, we can just check starting points within the first gap
            limit = pts[0][0] + perimeter // k
            for i in range(n):
                if pts[i][0] > limit: break
                
                count = 1
                curr_idx = i
                first_p = pts[i][1]
                last_p = first_p
                
                for _ in range(k - 1):
                    target_pos = pts[curr_idx][0] + d
                    # Binary search for first point with perimeter dist >= d
                    low, high = curr_idx + 1, n + i - 1
                    found_idx = -1
                    while low <= high:
                        mid = (low + high) // 2
                        if pts[mid % n][0] + (perimeter if mid >= n else 0) >= target_pos:
                            found_idx = mid
                            high = mid - 1
                        else:
                            low = mid + 1
                    
                    if found_idx == -1: break
                    
                    # Manhattan distance >= d is required. Since MD <= BD,
                    # we search forward from found_idx until MD >= d.
                    # On a square, MD >= d is usually satisfied quickly after BD >= d.
                    match = -1
                    for j in range(found_idx, n + i):
                        p_j = pts[j % n][1]
                        if get_md(last_p, p_j) >= d:
                            match = j
                            break
                        # Optimization: if BD gets too large, stop
                        if pts[j % n][0] + (perimeter if j >= n else 0) > pts[curr_idx][0] + 2 * d:
                            break
                            
                    if match != -1:
                        curr_idx = match
                        last_p = pts[curr_idx % n][1]
                        count += 1
                    else:
                        break
                
                if count == k and get_md(last_p, first_p) >= d:
                    return True
            return False

        ans = 0
        low, high = 0, 2 * side
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                ans = max(ans, 0)
                low = 1
                continue
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
# @lc code=end