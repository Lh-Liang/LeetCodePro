#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def build_graph(pairs, rates):
            g = defaultdict(list)
            for (a, b), r in zip(pairs, rates):
                g[a].append((b, r))
                g[b].append((a, 1.0/r))
            return g

        # Step 1: Day 1 conversions
        graph1 = build_graph(pairs1, rates1)
        max_after_day1 = defaultdict(float)
        max_after_day1[initialCurrency] = 1.0
        queue = deque([initialCurrency])
        while queue:
            cur = queue.popleft()
            for nxt, rate in graph1[cur]:
                amt = max_after_day1[cur] * rate
                if amt > max_after_day1[nxt] + 1e-9:
                    max_after_day1[nxt] = amt
                    queue.append(nxt)

        # Step 2: Day 2 conversions
        graph2 = build_graph(pairs2, rates2)
        max_final = defaultdict(float)
        for currency, amount in max_after_day1.items():
            max_final[currency] = max(max_final[currency], amount)
        queue = deque(max_final.keys())
        while queue:
            cur = queue.popleft()
            for nxt, rate in graph2[cur]:
                amt = max_final[cur] * rate
                if amt > max_final[nxt] + 1e-9:
                    max_final[nxt] = amt
                    queue.append(nxt)

        # Step 4: Compare with doing nothing (keeping initial amount)
        return max(1.0, max_final[initialCurrency])
# @lc code=end