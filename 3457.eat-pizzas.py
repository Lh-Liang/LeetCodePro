#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort pizzas by weight in descending order to maximize gains
        pizzas.sort(reverse=True)
        total_gain = 0
        # Process every 4 pizzas as a batch to determine daily gains
        for i in range(0, len(pizzas), 4):
            # Determine if it's an odd or even day based on batch index
            if (i // 4) % 2 == 0: # Odd day (1-indexed)
                total_gain += pizzas[i] # Add largest pizza's weight (Z)
            else: # Even day
                total_gain += pizzas[i + 1] # Add second largest pizza's weight (Y)
        return total_gain
# @lc code=end