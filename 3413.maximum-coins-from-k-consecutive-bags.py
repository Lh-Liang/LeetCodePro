#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
from typing import List

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Sort segments to process them in order
        coins.sort()
        n = len(coins)
        
        # Precompute prefix sums of coins for O(1) range sum calculation
        # prefix[i+1] = sum of coins in the first i segments
        prefix = [0] * (n + 1)
        for i in range(n):
            l, r, c = coins[i]
            prefix[i+1] = prefix[i] + (r - l + 1) * c
        
        max_total = 0
        
        # Case 1: Window starts at the beginning of segment i
        # Window is [coins[i][0], coins[i][0] + k - 1]
        right_ptr = 0
        for i in range(n):
            start = coins[i][0]
            end = start + k - 1
            
            # Advance right_ptr to find segments within the window
            while right_ptr < n and coins[right_ptr][1] <= end:
                right_ptr += 1
            
            # Full segments from i to right_ptr - 1
            current_sum = prefix[right_ptr] - prefix[i]
            
            # Partial segment at right_ptr (if it starts before 'end')
            if right_ptr < n and coins[right_ptr][0] <= end:
                current_sum += (end - coins[right_ptr][0] + 1) * coins[right_ptr][2]
            
            max_total = max(max_total, current_sum)
            
        # Case 2: Window ends at the end of segment i
        # Window is [coins[i][1] - k + 1, coins[i][1]]
        left_ptr = 0
        for i in range(n):
            end = coins[i][1]
            start = end - k + 1
            
            # Advance left_ptr to find segments within the window
            # We want the first segment that doesn't end before 'start'
            while left_ptr < n and coins[left_ptr][1] < start:
                left_ptr += 1
            
            # Full segments from left_ptr + 1 to i
            current_sum = prefix[i+1] - prefix[left_ptr+1]
            
            # Partial segment at left_ptr
            if left_ptr <= i:
                # The covered part of segment left_ptr is from max(l, start) to r
                covered_l = max(coins[left_ptr][0], start)
                current_sum += (coins[left_ptr][1] - covered_l + 1) * coins[left_ptr][2]
            
            max_total = max(max_total, current_sum)
            
        return max_total
# @lc code=end