#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Step 1: Create events for start and end of coin segments
        events = []
        for l, r, c in coins:
            events.append((l, c))  # Add coins starting from l
            events.append((r + 1, -c))  # Remove coins after r
        
        # Step 2: Sort events by position
        events.sort()
        
        # Step 3: Use a sliding window mechanism to track max sum over k consecutive bags
        current_coins = 0
        max_coins = 0
        current_window_sum = 0
        window_positions = []
        
        for position, change in events:
            while window_positions and window_positions[0] <= position - k:
                current_window_sum -= window_positions.pop(0)
            
            current_coins += change
            if change > 0:
                window_positions.append(change)
                current_window_sum += change
            
            max_coins = max(max_coins, current_window_sum)
            
        return max_coins
# @lc code=end