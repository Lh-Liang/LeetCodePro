#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
import collections
from typing import List, Dict

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def get_rates(start_node: str, pairs: List[List[str]], rates: List[float]) -> Dict[str, float]:
            adj = collections.defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                adj[u].append((v, r))
                adj[v].append((u, 1.0 / r))
            
            # Map to store the conversion rate from start_node to currency C
            # 1.0 start_node = rates_map[C] units of C
            rates_map = {start_node: 1.0}
            queue = collections.deque([start_node])
            
            while queue:
                curr = queue.popleft()
                for neighbor, rate in adj[curr]:
                    if neighbor not in rates_map:
                        rates_map[neighbor] = rates_map[curr] * rate
                        queue.append(neighbor)
            return rates_map

        # Day 1: Calculate how much of each currency we can have starting from initialCurrency
        day1_holdings = get_rates(initialCurrency, pairs1, rates1)
        
        # Day 2: Calculate conversion rates from initialCurrency to others on Day 2
        # This tells us the 'price' of 1.0 initialCurrency in terms of other currencies
        day2_rates = get_rates(initialCurrency, pairs2, rates2)
        
        max_final = 1.0
        
        # Try ending Day 1 with each possible currency and converting back on Day 2
        for currency, amount in day1_holdings.items():
            if currency in day2_rates:
                # If 1 Initial = day2_rates[currency] units of C,
                # then 1 unit of C = 1 / day2_rates[currency] units of Initial
                final_val = amount / day2_rates[currency]
                if final_val > max_final:
                    max_final = final_val
                    
        return max_final
# @lc code=end