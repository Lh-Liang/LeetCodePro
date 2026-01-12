#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
from typing import List

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        n = len(coins)
        
        def solve(intervals):
            m = len(intervals)
            res = 0
            curr_sum = 0
            right = 0
            for left in range(m):
                # Window starts at intervals[left][0], ends at intervals[left][0] + k - 1
                window_end = intervals[left][0] + k - 1
                while right < m and intervals[right][1] <= window_end:
                    curr_sum += (intervals[right][1] - intervals[right][0] + 1) * intervals[right][2]
                    right += 1
                
                # Partial segment at the end of the window
                extra = 0
                if right < m and intervals[right][0] <= window_end:
                    extra = (window_end - intervals[right][0] + 1) * intervals[right][2]
                
                res = max(res, curr_sum + extra)
                
                # Remove the current left segment from the sum for the next iteration
                curr_sum -= (intervals[left][1] - intervals[left][0] + 1) * intervals[left][2]
            return res

        # Case 1: Window starts at the beginning of some segment
        ans = solve(coins)
        
        # Case 2: Window ends at the end of some segment
        # We transform the segments to represent them from right to left
        reversed_coins = []
        for l, r, c in coins:
            reversed_coins.append([-r, -l, c])
        reversed_coins.sort()
        
        ans = max(ans, solve(reversed_coins))
        
        return ans
# @lc code=end