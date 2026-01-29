#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
import math

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort descending to pick the largest weights first
        pizzas.sort(reverse=True)
        
        n = len(pizzas)
        days = n // 4
        # Number of odd-numbered days (1, 3, 5...)
        odd_days = (days + 1) // 2
        # Number of even-numbered days (2, 4, 6...)
        even_days = days // 2
        
        # For odd days, we gain weight Z (the heaviest of the 4).
        # We take the top 'odd_days' pizzas.
        total_gain = sum(pizzas[:odd_days])
        
        # For even days, we gain weight Y (the second heaviest).
        # To maximize Y, we must 'sacrifice' one heavier pizza to be Z for each even day.
        # We start picking from index 'odd_days', skipping one for every one we take.
        # Indices: odd_days + 1, odd_days + 3, ..., odd_days + 2*even_days - 1
        start_idx = odd_days
        even_day_gains = pizzas[start_idx + 1 : start_idx + 1 + 2 * even_days : 2]
        total_gain += sum(even_day_gains)
        
        return total_gain
# @lc code=end