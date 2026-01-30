#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        pizzas.sort()
        total = 0
        days = n // 4
        for d in range(days):
            # For each day, pick the largest 4 remaining pizzas
            idx = n - (d + 1) * 4
            group = pizzas[idx:idx + 4]
            group.sort()
            if d % 2 == 0:  # odd day (1-indexed)
                total += group[3]
            else:           # even day
                total += group[2]
        return total
# @lc code=end