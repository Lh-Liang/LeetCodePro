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
        res = 0
        days = n // 4
        for i in range(days):
            group = pizzas[n - 4*(i+1): n - 4*i]
            group.sort()
            if i % 2 == 0:
                res += group[3]
            else:
                res += group[2]
        # Verification: ensure all pizzas used and correct group sizes
        assert n == days * 4
        return res
# @lc code=end