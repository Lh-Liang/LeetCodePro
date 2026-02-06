#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse=True)  # Step 1: Sort in descending order.
        total_gain = 0
        # Iterate over the sorted pizzas in chunks of 4.
        for i in range(0, len(pizzas), 4):
            if (i // 4) % 2 == 0:  # Step 2: Check if it's an odd day (0-indexed).
                total_gain += pizzas[i]     # Gain Z on odd days (largest)
            else:
                total_gain += pizzas[i + 1] # Gain Y on even days (second largest)
        return total_gain # Step 3: Return total gained weight.
# @lc code=end