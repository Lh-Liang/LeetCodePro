#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def maxAmount(
        self,
        initialCurrency: str,
        pairs1: List[List[str]],
        rates1: List[float],
        pairs2: List[List[str]],
        rates2: List[float],
    ) -> float:

        def build_graph(pairs: List[List[str]], rates: List[float]) -> Dict[str, List[tuple]]:
            g = defaultdict(list)
            for (a, b), r in zip(pairs, rates):
                g[a].append((b, r))
                g[b].append((a, 1.0 / r))
            return g

        def compute_rates_from_start(start: str, g: Dict[str, List[tuple]]) -> Dict[str, float]:
            rate = {start: 1.0}
            q = deque([start])
            while q:
                u = q.popleft()
                for v, w in g.get(u, []):
                    if v in rate:
                        continue
                    rate[v] = rate[u] * w
                    q.append(v)
            return rate

        g1 = build_graph(pairs1, rates1)
        g2 = build_graph(pairs2, rates2)

        day1 = compute_rates_from_start(initialCurrency, g1)
        day2 = compute_rates_from_start(initialCurrency, g2)

        ans = 1.0  # do nothing both days
        for cur, amt_after_day1 in day1.items():
            if cur in day2:  # can convert back to initial on day 2
                ans = max(ans, amt_after_day1 / day2[cur])

        return ans
# @lc code=end
