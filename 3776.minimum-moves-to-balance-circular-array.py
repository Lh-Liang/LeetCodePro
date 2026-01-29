#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
from typing import List
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        if n == 0 or all(b >= 0 for b in balance):
            return 0
        total_sum = sum(balance)
        if total_sum < 0:
            return -1 

        total_moves = 0
        current_deficit = 0
        # Traverse over each element assuming circular behavior with twice length 
        for i in range(2 * n):
            index = i % n
            if balance[index] < 0:
                current_deficit += balance[index]
            elif current_deficit < 0 and balance[index] > 0:
                move = min(balance[index], -current_deficit)
                total_moves += move
                current_deficit += move
                balance[index] -= move
            # Check if we have completed one full circle and still have deficit
            if i >= n and current_deficit < 0:
                return -1 
        return total_moves # Return total moves made once balanced or verified impossible.
# @lc code=end