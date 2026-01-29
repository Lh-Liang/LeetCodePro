#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
import bisect
from typing import List

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Sort segments by start position to enable binary search and prefix sums
        coins.sort()
        n = len(coins)
        
        # Extract components for easier access
        l = [c[0] for c in coins]
        r = [c[1] for c in coins]
        c = [c[2] for c in coins]
        
        # Prefix sum of coins: pre[i] is sum of first i segments
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + (r[i] - l[i] + 1) * c[i]
            
        max_coins = 0
        
        # Case 1: Window starts at the beginning of segment i [l[i], l[i] + k - 1]
        for i in range(n):
            R = l[i] + k - 1
            # Find the largest index j such that segment j starts at or before R
            j = bisect.bisect_right(l, R) - 1
            
            # Sum of fully contained segments from i to j-1
            # pre[j] is sum of segments 0 to j-1; pre[i] is sum of segments 0 to i-1
            current = pre[j] - pre[i]
            # Add partial or full contribution of segment j (capped at R)
            current += (min(r[j], R) - l[j] + 1) * c[j]
            
            if current > max_coins:
                max_coins = current
                
        # Case 2: Window ends at the end of segment i [r[i] - k + 1, r[i]]
        for i in range(n):
            L = r[i] - k + 1
            # Find the smallest index j such that segment j ends at or after L
            j = bisect.bisect_left(r, L)
            
            # Sum of fully contained segments from j+1 to i
            # pre[i+1] is sum of segments 0 to i; pre[j+1] is sum of segments 0 to j
            current = pre[i+1] - pre[j+1]
            # Add partial or full contribution of segment j (starting from L)
            current += (r[j] - max(l[j], L) + 1) * c[j]
            
            if current > max_coins:
                max_coins = current
                
        return max_coins
# @lc code=end