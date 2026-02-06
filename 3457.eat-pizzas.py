#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Step 1: Sort pizzas by weight
        pizzas.sort()
        n = len(pizzas)
        total_weight = 0
        
        # Step 2: Calculate total max weight gained by eating in sets of four
        for i in range(0, n, 4):
            # Determine if it's an odd or even day based on one-indexed logic
            # On odd days, add Z (heaviest)
            if i // 4 % 2 == 0:
                total_weight += pizzas[i+3]
            # On even days, add Y (second heaviest)
            else:
                total_weight += pizzas[i+2]
        
        return total_weight
# @lc code=end