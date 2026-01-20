#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)
        days = n // 4
        odd_days = (days + 1) // 2
        even_days = days // 2
        
        total_weight = 0
        
        # Use the largest pizzas for the odd days
        # We take the top 'odd_days' elements from the end
        # Current index pointer starts at the last element
        idx = n - 1
        for _ in range(odd_days):
            total_weight += pizzas[idx]
            idx -= 1
            
        # Use the next largest pizzas for the even days
        # For even days, we need pairs (Y, Z) where we get Y.
        # To maximize Y, we take the largest available pair and the second largest is Y.
        # So we skip one (the Z) and take the next (the Y).
        for _ in range(even_days):
            idx -= 1 # This is the Z (sacrifice)
            total_weight += pizzas[idx] # This is the Y (gain)
            idx -= 1
            
        return total_weight
# @lc code=end