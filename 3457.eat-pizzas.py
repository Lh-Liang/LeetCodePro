#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort pizzas in descending order
        pizzas.sort(reverse=True)
        # Sum every other element starting from index 0
        # This selects k elements where k = n / 4
        return sum(pizzas[::2])