#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#
# @lc code=start
from typing import List, Dict

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        from collections import defaultdict, deque
        
        def build_graph(pairs, rates):
            graph = defaultdict(list)
            for (a,b), r in zip(pairs, rates):
                graph[a].append((b, r))
                graph[b].append((a, 1.0/r))
            return graph
        
        def get_max_amounts(graph, start, amount):
            max_amount = defaultdict(float)
            max_amount[start] = amount
            queue = deque([start])
            while queue:
                curr = queue.popleft()
                for neighbor, rate in graph[curr]:
                    new_amount = max_amount[curr] * rate
                    if new_amount > max_amount[neighbor]:
                        max_amount[neighbor] = new_amount
                        queue.append(neighbor)
            return max_amount
        
        graph1 = build_graph(pairs1, rates1)
        graph2 = build_graph(pairs2, rates2)
        
        # Day 1: get max amount of all currencies from initialCurrency
        max_after_day1 = get_max_amounts(graph1, initialCurrency, 1.0)
        result = max_after_day1[initialCurrency]  # If we do nothing
        
        # For each currency we could have after day 1, maximize back to initialCurrency after day 2
        for currency, amount in max_after_day1.items():
            max_after_day2 = get_max_amounts(graph2, currency, amount)
            result = max(result, max_after_day2[initialCurrency])
        return result
# @lc code=end