# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        from collections import defaultdict
        
        def maximize_conversion(pairs, rates, initial_values):
            # Initialize max values with given initial values or -inf if not present
            max_values = defaultdict(lambda: -float('inf'))
            max_values.update(initial_values)
            
            # Iterate multiple times to ensure all paths are considered
            for _ in range(len(pairs)):
                updated = False
                for (start, end), rate in zip(pairs, rates):
                    if max_values[start] != -float('inf') and max_values[end] < max_values[start] * rate:
                        max_values[end] = max_values[start] * rate
                        updated = True
                if not updated:
                    break
            return max_values
        
        # Start with initial currency having value of 1.0
        day_1_starting = {initialCurrency: 1.0}
        # Perform conversion maximization for day 1
        max_after_day_1 = maximize_conversion(pairs1, rates1, day_1_starting)
        
        # Use results from day 1 as starting point for day 2 conversions
        # Perform conversion maximization for day 2 using day 1 results as starting values
        max_after_day_2 = maximize_conversion(pairs2, rates2, max_after_day_1)
        
        # Return maximum amount of initialCurrency after two days of conversions
        return max_after_day_2.get(initialCurrency, -float('inf'))
# @lc code=end