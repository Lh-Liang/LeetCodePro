#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

import bisect

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Map 2D points to 1D positions along the perimeter [0, 4 * side)
        pos_list = []
        for x, y in points:
            if y == 0:
                p = x
            elif x == side:
                p = side + y
            elif y == side:
                p = 3 * side - x
            else: # x == 0
                p = 4 * side - y
            pos_list.append(p)
        
        pos_list.sort()
        n = len(pos_list)
        L = 4 * side

        def can_place(d):
            # If a solution exists, one point must be in the first 1/k of the perimeter
            # starting from the first point in our sorted list.
            max_start_pos = pos_list[0] + (L // k)
            
            for i in range(n):
                if pos_list[i] > max_start_pos:
                    break
                
                start_val = pos_list[i]
                count = 1
                curr_idx = i
                last_pos = start_val
                
                # Greedily pick the remaining k-1 points
                possible = True
                for _ in range(k - 1):
                    target = last_pos + d
                    # Find the first point >= last_pos + d
                    next_idx = bisect.bisect_left(pos_list, target, lo=curr_idx + 1)
                    if next_idx == n:
                        possible = False
                        break
                    last_pos = pos_list[next_idx]
                    curr_idx = next_idx
                
                # Check circular distance back to the starting point
                if possible and (start_val + L - last_pos >= d):
                    return True
            return False

        # Binary search for the maximum possible minimum distance
        low = 1
        high = side
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
# @lc code=end