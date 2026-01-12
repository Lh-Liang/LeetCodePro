#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort pizzas in descending order to pick the heaviest ones first
        pizzas.sort(reverse=True)
        
        n = len(pizzas)
        k = n // 4
        # Number of odd-numbered days (1-indexed: 1, 3, 5...)
        k_odd = (k + 1) // 2
        # Number of even-numbered days (1-indexed: 2, 4, 6...)
        k_even = k // 2
        
        # On odd days, we gain the weight of the largest pizza (Z).
        # We take the top k_odd pizzas for these days.
        total_weight = sum(pizzas[:k_odd])
        
        # On even days, we gain the weight of the second largest pizza (Y).
        # To maximize Y, we pair the largest remaining pizzas: (Z1, Y1), (Z2, Y2)...
        # This means we skip one pizza (the Z) and take the next (the Y).
        # We start picking from index k_odd.
        # Indices to pick: k_odd + 1, k_odd + 3, ..., k_odd + 2*k_even - 1
        start_idx = k_odd + 1
        end_idx = k_odd + 2 * k_even
        even_day_weights = pizzas[start_idx : end_idx : 2]
        
        total_weight += sum(even_day_weights)
        
        return total_weight
# @lc code=end