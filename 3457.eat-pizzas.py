#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        n = len(pizzas)
        d = n // 4
        odd = (d + 1) // 2  # number of odd days
        even = d // 2        # number of even days
        
        # Odd day contributions: top 'odd' pizzas (we gain the max Z)
        result = sum(pizzas[:odd])
        
        # Even day contributions: from the remaining pizzas for even days,
        # we pair them (Z, Y) and gain Y (every other starting from odd+1)
        # Indices: odd+1, odd+3, ..., odd+2*even-1
        result += sum(pizzas[odd + 1: odd + 2 * even: 2])
        
        return result
# @lc code=end