#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def get_max_rates(start_currency, pairs, rates, initial_amt):
            graph = defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                graph[u].append((v, r))
                graph[v].append((u, 1.0 / r))
            
            max_amounts = {start_currency: initial_amt}
            queue = deque([start_currency])
            
            while queue:
                curr = queue.popleft()
                for neighbor, rate in graph[curr]:
                    new_amt = max_amounts[curr] * rate
                    if neighbor not in max_amounts:
                        max_amounts[neighbor] = new_amt
                        queue.append(neighbor)
            return max_amounts

        # Day 1: Calculate max amount of every currency starting from initialCurrency
        day1_amounts = get_max_rates(initialCurrency, pairs1, rates1, 1.0)
        
        max_final_amt = 0.0
        
        # Day 2: For each currency reached on Day 1, find max initialCurrency possible
        for intermediate_curr, amt in day1_amounts.items():
            day2_rates = get_max_rates(intermediate_curr, pairs2, rates2, amt)
            if initialCurrency in day2_rates:
                max_final_amt = max(max_final_amt, day2_rates[initialCurrency])
            else:
                # If we can't convert back, we still have the amount from day 1 
                # but the problem implies we want the initialCurrency specifically.
                # However, if intermediate == initial, day2_rates will contain it.
                # If not, and we can't reach initial, this path is invalid for the goal.
                pass
                
        return max_final_amt
# @lc code=end