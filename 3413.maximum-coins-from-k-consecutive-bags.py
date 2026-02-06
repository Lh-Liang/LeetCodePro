#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Map to store total coins at each position
        position_coins = defaultdict(int)
        
        # Fill map with coin values from segments
        for li, ri, ci in coins:
            for pos in range(li, ri + 1):
                position_coins[pos] += ci
        
        # Sort positions for sliding window traversal
        sorted_positions = sorted(position_coins.keys())
        
        max_coins = 0
        current_sum = 0
        left = 0
        
        # Use sliding window over sorted positions to find max sum of k consecutive positions
        for right in range(len(sorted_positions)):
            current_sum += position_coins[sorted_positions[right]]
            
            if right - left + 1 > k:
                current_sum -= position_coins[sorted_positions[left]]
                left += 1
            
            if right - left + 1 == k:
                max_coins = max(max_coins, current_sum)
                
        return max_coins
# @lc code=end