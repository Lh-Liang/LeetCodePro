#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
import math

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        n = len(pizzas)
        total_days = n // 4
        
        # Number of odd and even days
        odd_days = (total_days + 1) // 2
        even_days = total_days // 2
        
        max_total_weight = 0
        
        # For odd days, we take the largest available pizzas as 'Z'
        for i in range(odd_days):
            max_total_weight += pizzas[i]
            
        # For even days, we need to pick 'Y'. 
        # Each even day requires skipping one larger pizza (to be 'Z') 
        # and taking the next largest (to be 'Y').
        current_idx = odd_days
        for _ in range(even_days):
            # Skip one (the Z for this even day) and take the next (the Y)
            max_total_weight += pizzas[current_idx + 1]
            current_idx += 2
            
        return max_total_weight
# @lc code=end