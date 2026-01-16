#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#
# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Sort coins by their starting position
        coins.sort()
        n = len(coins)
        
        # Precompute prefix sums for efficient range sum queries
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (coins[i][1] - coins[i][0] + 1) * coins[i][2]
        
        max_coins = 0
        
        # Try each coin segment as the starting point of our k consecutive bags
        for i in range(n):
            # Binary search to find the rightmost segment that could be part of our k consecutive bags
            left, right = i, n - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                # Check if we can take all segments from i to mid
                if coins[mid][0] - coins[i][0] + 1 <= k:
                    result = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            if result == -1:
                continue
                
            # Calculate coins for segments from i to result
            total_coins = prefix_sum[result + 1] - prefix_sum[i]
            
            # Adjust for the case where we don't need all bags in the last segment
            if coins[result][1] - coins[i][0] + 1 > k:
                # We need to subtract the excess bags from the last segment
                excess_length = (coins[result][1] - coins[i][0] + 1) - k
                excess_coins = excess_length * coins[result][2]
                total_coins -= excess_coins
            
            max_coins = max(max_coins, total_coins)
        
        return max_coins
# @lc code=end