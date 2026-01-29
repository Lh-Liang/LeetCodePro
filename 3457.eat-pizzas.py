# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
from typing import List

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort pizzas in descending order
        sorted_pizzas = sorted(pizzas, reverse=True)
        total_weight_gain = 0
        
        # Iterate over groups of four pizzas at a time
        for i in range(0, len(sorted_pizzas), 4):
            # Odd days (1-indexed): Gain weight of heaviest pizza Z
            if (i // 4) % 2 == 0:
                total_weight_gain += sorted_pizzas[i]
            # Even days (1-indexed): Gain weight of second heaviest pizza Y
            else:
                total_weight_gain += sorted_pizzas[i + 1]
        
        return total_weight_gain
# @lc code=end