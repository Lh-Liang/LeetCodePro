#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Step 1: Create events from segments
        events = []
        for l, r, c in coins:
            events.append((l, c))       # Start event adds coins
            events.append((r + 1, -c))  # End event removes coins (after r)
        
        # Step 2: Sort events by position
        events.sort()
        
        # Step 3: Sweep line with current coin count and calculate sums.
        current_sum = 0
        max_coins = 0
        sums_at_positions = []
        last_position = None
        
        for pos, change in events:
            if last_position is not None and pos != last_position:
                sums_at_positions.append((last_position, current_sum))
            current_sum += change
            last_position = pos
        
        # After processing all events, check final position's sum as well if not added.
        if last_position is not None:
            sums_at_positions.append((last_position, current_sum))
        
        # Step 4: Calculate max using sliding window over recorded sums.
        max_coins = 0
        start_idx = 0      # Start of sliding window index on sums_at_positions array.
        window_sum = 0     # Sum within current window size <= k.
        num_positions_covered = 0   # Track number of actual positions covered in window.
        
        for end_idx in range(len(sums_at_positions)):
            pos_end, value_end = sums_at_positions[end_idx]
            while num_positions_covered < k and end_idx < len(sums_at_positions):
                if end_idx > start_idx:
                    num_positions_covered += (sums_at_positions[end_idx][0] - sums_at_positions[end_idx - 1][0])
                else:
                    num_positions_covered += 1  # First element starts covering one position.
                window_sum += value_end
                end_idx += 1    
            while num_positions_covered > k:
                pos_start, value_start = sums_at_positions[start_idx]
                if start_idx + 1 < len(sums_at_positions):
                    next_pos_start = sums_at_positions[start_idx + 1][0]
                    num_positions_covered -= (next_pos_start - pos_start)
                else:
                    num_positions_covered -= (pos_end - pos_start)
                window_sum -= value_start
                start_idx += 1   
            max_coins = max(max_coins, window_sum)
            if end_idx < len(sums_at_positions):
                end_idx -= 1   # Correct loop increment effect when breaking out early.																	    	      	          	             	         	          	          	         	          	         	       	       return max_coins
# @lc code=end