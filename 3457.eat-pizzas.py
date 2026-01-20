#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
from typing import List

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)
        n = len(pizzas)
        k = n // 4
        odd_days = (k + 1) // 2
        even_days = k // 2
        m = odd_days + 2 * even_days
        sum_top = sum(pizzas[:m])
        sacrificed = 0
        start = odd_days
        for i in range(even_days):
            sacrificed += pizzas[start + 2 * i]
        return sum_top - sacrificed

# @lc code=end