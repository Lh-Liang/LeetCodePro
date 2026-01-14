#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
from bisect import bisect_right, bisect_left

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        n = len(coins)
        
        # Prefix sum of total coins in segments
        prefix = [0] * (n + 1)
        for i in range(n):
            l, r, c = coins[i]
            prefix[i + 1] = prefix[i] + (r - l + 1) * c
        
        result = 0
        
        lefts = [coins[i][0] for i in range(n)]
        rights = [coins[i][1] for i in range(n)]
        
        # Try window starting at each segment's left boundary
        for i in range(n):
            window_end = coins[i][0] + k - 1
            j = bisect_right(lefts, window_end) - 1
            
            if coins[j][1] <= window_end:
                # Segment j is fully included
                total = prefix[j + 1] - prefix[i]
            else:
                # Segment j is partially included
                total = prefix[j] - prefix[i]
                total += (window_end - coins[j][0] + 1) * coins[j][2]
            result = max(result, total)
        
        # Try window ending at each segment's right boundary
        for i in range(n):
            window_start = coins[i][1] - k + 1
            j = bisect_left(rights, window_start)
            
            if coins[j][0] >= window_start:
                # Segment j is fully included
                total = prefix[i + 1] - prefix[j]
            else:
                # Segment j is partially included
                total = prefix[i + 1] - prefix[j + 1]
                total += (coins[j][1] - window_start + 1) * coins[j][2]
            result = max(result, total)
        
        return result
# @lc code=end