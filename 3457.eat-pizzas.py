#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
from typing import List

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)
        m = n // 4
        odd_days = (m + 1) // 2
        even_days = m // 2

        low, high = 0, n - 1
        ans = 0

        # Allocate pizzas for odd days: gain the largest Z, waste 3 smallest as fillers
        for _ in range(odd_days):
            ans += pizzas[high]
            high -= 1
            low += 3

        # Allocate pizzas for even days: take two largest (Y,Z), gain Y (= second largest),
        # and waste 2 smallest as fillers
        for _ in range(even_days):
            ans += pizzas[high - 1]
            high -= 2
            low += 2

        return ans
# @lc code=end
