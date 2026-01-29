#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort pizzas in descending order to pick the heaviest ones greedily
        pizzas.sort(reverse=True)
        
        n = len(pizzas)
        total_days = n // 4
        # Number of odd-numbered days (1, 3, 5...)
        odd_days = (total_days + 1) // 2
        # Number of even-numbered days (2, 4, 6...)
        even_days = total_days // 2
        
        # For odd days, we gain the largest pizza (Z).
        # We take the top 'odd_days' pizzas.
        total_gain = sum(pizzas[:odd_days])
        
        # For even days, we gain the second largest pizza (Y).
        # For each even day, we need one pizza to be Z (larger than Y).
        # So we skip one, take one, skip one, take one...
        # Starting from the index after the odd_day pizzas.
        current_idx = odd_days
        for _ in range(even_days):
            # Skip one (to be Z), take the next (to be Y)
            current_idx += 1
            total_gain += pizzas[current_idx]
            current_idx += 1
            
        return total_gain
# @lc code=end