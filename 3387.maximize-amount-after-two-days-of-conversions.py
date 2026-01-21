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
        def get_reachable_rates(start_currency: str, pairs: List[List[str]], rates: List[float]) -> dict:
            # Build an adjacency list representing the conversion graph for the day
            adj = collections.defaultdict(list)
            for i in range(len(pairs)):
                u, v = pairs[i]
                r = rates[i]
                adj[u].append((v, r))
                adj[v].append((u, 1.0 / r))
            
            # Use BFS to find the conversion rate from start_currency to all reachable currencies
            # Since there are no contradictions, the first time we visit a node, we find the unique rate.
            rates_from_start = {start_currency: 1.0}
            queue = collections.deque([start_currency])
            while queue:
                u = queue.popleft()
                for v, r in adj[u]:
                    if v not in rates_from_start:
                        rates_from_start[v] = rates_from_start[u] * r
                        queue.append(v)
            return rates_from_start

        # Step 1: Calculate the amount of every possible currency we can have after Day 1.
        # dist1[C] is the amount of currency C we have per 1.0 unit of initialCurrency.
        dist1 = get_reachable_rates(initialCurrency, pairs1, rates1)
        
        # Step 2: Calculate the conversion rates from initialCurrency to others on Day 2.
        # dist2[C] is the amount of currency C we get per 1.0 unit of initialCurrency on Day 2.
        # The rate to convert C back to initialCurrency is therefore 1.0 / dist2[C].
        dist2 = get_reachable_rates(initialCurrency, pairs2, rates2)

        # Step 3: Maximize the final amount of initialCurrency.
        # We can always choose to do nothing and keep 1.0 unit of initialCurrency.
        max_amt = 1.0
        for currency, amount_after_day1 in dist1.items():
            # If we can convert this currency back to initialCurrency on Day 2
            if currency in dist2:
                # Final amount = (amount of currency C) * (rate C -> initialCurrency on Day 2)
                final_amount = amount_after_day1 / dist2[currency]
                if final_amount > max_amt:
                    max_amt = final_amount
        
        return max_amt
# @lc code=end