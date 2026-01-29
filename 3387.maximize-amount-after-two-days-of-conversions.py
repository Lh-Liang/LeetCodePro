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
        def get_rates(start_node: str, pairs: List[List[str]], rates: List[float]) -> dict:
            # Build adjacency list for undirected graph with rates
            adj = defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                adj[u].append((v, r))
                adj[v].append((u, 1.0 / r))
            
            # Map to store conversion rate from start_node to currency
            # Since rates are consistent, any traversal (BFS/DFS) works
            rates_map = {start_node: 1.0}
            queue = deque([start_node])
            
            while queue:
                u = queue.popleft()
                for v, r in adj[u]:
                    if v not in rates_map:
                        rates_map[v] = rates_map[u] * r
                        queue.append(v)
            return rates_map

        # Day 1: Calculate how much of each currency we can have 
        # starting with 1.0 of initialCurrency
        day1_amounts = get_rates(initialCurrency, pairs1, rates1)
        
        # Day 2: Calculate the conversion rate from initialCurrency to other currencies.
        # To convert currency C back to initialCurrency, the rate is 1 / day2_rates[C].
        day2_rates = get_rates(initialCurrency, pairs2, rates2)
        
        max_total = 1.0
        
        # For every currency held at the end of Day 1, check if it can reach 
        # initialCurrency on Day 2 and calculate the final amount.
        for curr, amount in day1_amounts.items():
            if curr in day2_rates:
                # Final amount = (amount of curr) * (rate to convert curr to initialCurrency)
                # rate(curr -> initial) = 1 / rate(initial -> curr)
                final_amount = amount / day2_rates[curr]
                if final_amount > max_total:
                    max_total = final_amount
                
        return max_total
# @lc code=end