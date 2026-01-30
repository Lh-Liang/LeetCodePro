#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Initialize max position based on constraints
        max_position = max(ri for li, ri, ci in coins) + 1
        # Use a difference array approach to track coin additions
        diff = [0] * (max_position + 1)
        # Populate the difference array with coin values at start and end+1 positions
        for li, ri, ci in coins:
            diff[li] += ci
            if ri + 1 <= max_position:
                diff[ri + 1] -= ci
        # Create an array representing total coins at each position after applying differences
        total_coins = [0] * (max_position + 1)
        total_coins[0] = diff[0]
        for i in range(1, max_position):
            total_coins[i] = total_coins[i - 1] + diff[i]
        # Use sliding window technique to find maximum sum of k consecutive positions
        current_sum = sum(total_coins[:k])
        max_sum = current_sum
        for i in range(k, max_position):
            current_sum += total_coins[i] - total_coins[i - k]
            max_sum = max(max_sum, current_sum)
        return max_sum
# @lc code=end