#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        n = len(pizzas)
        d = n // 4
        odd_days = (d + 1) // 2
        even_days = d // 2
        
        # Gain from odd days: top odd_days pizzas
        total = sum(pizzas[:odd_days])
        
        # Gain from even days: indices odd_days+1, odd_days+3, ...
        total += sum(pizzas[odd_days + 1 : odd_days + 2 * even_days : 2])
        
        return total
# @lc code=end