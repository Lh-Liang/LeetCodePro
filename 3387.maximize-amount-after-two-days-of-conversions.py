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
            adj = collections.defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                adj[u].append((v, r))
                adj[v].append((u, 1.0 / r))
            
            # Map to store unique conversion rate from start_node to reachable currencies
            rates_map = {start_node: 1.0}
            queue = collections.deque([start_node])
            
            while queue:
                u = queue.popleft()
                for v, r in adj[u]:
                    if v not in rates_map:
                        rates_map[v] = rates_map[u] * r
                        queue.append(v)
            return rates_map

        # Day 1: Max amount of each currency we can get from 1.0 initialCurrency
        day1_amounts = get_reachable_rates(initialCurrency, pairs1, rates1)
        
        # Day 2: Rate to get from initialCurrency to other currencies on Day 2
        # Converting 'curr' back to 'initialCurrency' uses 1 / day2_rates[curr]
        day2_rates = get_reachable_rates(initialCurrency, pairs2, rates2)
        
        max_total = 1.0
        
        for curr, amount in day1_amounts.items():
            if curr in day2_rates:
                # Final amount = amount_held * rate_to_convert_back
                # rate_to_convert_back = 1.0 / (rate_from_initial_to_curr_on_day2)
                total = amount / day2_rates[curr]
                if total > max_total:
                    max_total = total
                    
        return max_total
# @lc code=end