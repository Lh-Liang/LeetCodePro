#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
from typing import List
import functools

class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # Precompute prefix sums of time to quickly calculate segment speeds
        prefix_time = [0] * (n + 1)
        for i in range(n):
            prefix_time[i + 1] = prefix_time[i] + time[i]

        def get_speed(start_idx, end_idx):
            # Speed of segment starting at end_idx, where signs between start_idx and end_idx were removed
            return prefix_time[end_idx + 1] - prefix_time[start_idx + 1]

        @functools.lru_cache(None)
        def dp(rem, last, prev):
            # rem: number of signs removed from indices 1...n-2
            # last: index of the last sign kept
            # prev: index of the sign kept before 'last'
            
            if last == n - 1:
                return 0 if rem == k else float('inf')
            
            res = float('inf')
            # Try keeping the next sign 'nxt'
            for nxt in range(last + 1, n):
                removed_now = nxt - last - 1
                if rem + removed_now <= k:
                    # Calculate the cost of the segment [pos[last], pos[nxt]]
                    # If last is 0, speed is time[0]. Otherwise, speed is sum(time[prev+1...last])
                    speed = time[0] if last == 0 else get_speed(prev, last)
                    cost = (position[nxt] - position[last]) * speed
                    
                    sub = dp(rem + removed_now, nxt, last)
                    if sub != float('inf'):
                        res = min(res, cost + sub)
            return res

        ans = dp(0, 0, -1)
        return int(ans)
# @lc code=end