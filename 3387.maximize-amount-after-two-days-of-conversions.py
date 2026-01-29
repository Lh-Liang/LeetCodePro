#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
import collections
from typing import List

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def get_reachable_rates(start_node: str, pairs: List[List[str]], rates: List[float]) -> dict:
            # Build an adjacency list for the conversion graph
            graph = collections.defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                graph[u].append((v, r))
                graph[v].append((u, 1.0 / r))
            
            # Map to store the conversion rate from start_node to each reachable currency
            # Initialized with start_node having a rate of 1.0
            rates_map = {start_node: 1.0}
            queue = collections.deque([start_node])
            
            while queue:
                u = queue.popleft()
                current_rate = rates_map[u]
                for v, r in graph[u]:
                    if v not in rates_map:
                        rates_map[v] = current_rate * r
                        queue.append(v)
            return rates_map

        # Day 1: Find all currencies reachable from initialCurrency and their amounts
        day1_rates = get_reachable_rates(initialCurrency, pairs1, rates1)
        
        # Day 2: Find conversion rates from initialCurrency to other currencies using Day 2 rules
        # We calculate initial -> X so we can easily derive X -> initial as 1 / (initial -> X)
        day2_rates = get_reachable_rates(initialCurrency, pairs2, rates2)

        max_final_amount = 1.0
        
        # For every currency we could hold at the end of Day 1
        for currency, amount_after_day1 in day1_rates.items():
            # If this currency can be converted back to initialCurrency on Day 2
            if currency in day2_rates:
                # Rate from currency back to initialCurrency on Day 2
                rate_back = 1.0 / day2_rates[currency]
                total = amount_after_day1 * rate_back
                if total > max_final_amount:
                    max_final_amount = total
        
        return float(max_final_amount)
# @lc code=end