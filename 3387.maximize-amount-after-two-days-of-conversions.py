#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        from collections import defaultdict
        import math
        
        # Function to perform Bellman-Ford for a single day's graph
        def bellman_ford(start_amounts, pairs, rates):
            # Initialize distances with provided start amounts
            max_amounts = start_amounts.copy()
            
            # Relax edges up to n-1 times (where n is number of currencies)
            for _ in range(len(pairs)):
                new_amounts = max_amounts.copy()
                for (src, dst), rate in zip(pairs, rates):
                    if max_amounts[src] != -math.inf:
                        new_amounts[dst] = max(new_amounts[dst], max_amounts[src] * rate)
                max_amounts = new_amounts
            return max_amounts
        
        # Day 1 conversions starting with initial amount in initialCurrency
        start_amounts_day1 = defaultdict(lambda: -math.inf)
        start_amounts_day1[initialCurrency] = 1.0
        day1_results = bellman_ford(start_amounts_day1, pairs1, rates1)
        
        # Use results from day 1 as starting point for day 2 conversions
        day2_results = bellman_ford(day1_results, pairs2, rates2)
        
        # Calculate final maximum value achievable in initial currency after two days
        return day2_results[initialCurrency]
# @lc code=end