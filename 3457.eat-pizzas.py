#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort descending to pick the largest weights greedily
        pizzas.sort(reverse=True)
        
        n = len(pizzas)
        total_days = n // 4
        odd_days = (total_days + 1) // 2
        even_days = total_days // 2
        
        # Gain from odd days: The absolute heaviest pizzas
        # These are the first 'odd_days' elements in the sorted list
        total_weight = sum(pizzas[:odd_days])
        
        # Gain from even days: The second heaviest in their respective groups
        # We must skip one 'Z' pizza for every 'Y' pizza we take.
        # Starting after the odd_days pizzas, we take every second pizza.
        even_start_idx = odd_days + 1
        even_end_idx = odd_days + 2 * even_days
        total_weight += sum(pizzas[even_start_idx : even_end_idx : 2])
        
        return total_weight
# @lc code=end