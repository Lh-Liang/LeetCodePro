#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Convert 2D points on the square boundary to 1D perimeter coordinates
        d_coords = []
        for x, y in points:
            if y == 0:
                d = x
            elif x == side:
                d = side + y
            elif y == side:
                d = 3 * side - x
            else: # x == 0
                d = 4 * side - y
            d_coords.append(d)
        
        d_coords.sort()
        n = len(d_coords)
        perimeter = 4 * side

        def check(X):
            # Precompute next[i]: the index of the first point j such that d_j >= d_i + X
            nxt = [n] * n
            r = 0
            for l in range(n):
                while r < n and d_coords[r] < d_coords[l] + X:
                    r += 1
                nxt[l] = r
            
            # We only need to try starting points in the first 'gap'
            # If a solution exists, at least one point must fall in [d_0, d_0 + X]
            for i in range(n):
                if d_coords[i] > d_coords[0] + X:
                    break
                
                curr = i
                count = 1
                # Greedily pick k-1 more points
                for _ in range(k - 1):
                    curr = nxt[curr]
                    if curr == n: break
                    count += 1
                
                # Check if k points were picked and the wrap-around distance is >= X
                if count == k and perimeter - (d_coords[curr] - d_coords[i]) >= X:
                    return True
            return False

        # Binary search for the maximum minimum distance X
        low = 1
        high = side # Max possible min distance for k >= 4 is 'side'
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
# @lc code=end