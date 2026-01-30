#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions

# @lc code=start
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        from collections import defaultdict, deque
        # Helper function to run BFS
        def bfs(start_currency, pairs, rates):
            graph = defaultdict(list)
            for (start, target), rate in zip(pairs, rates):
                graph[start].append((target, rate))
                graph[target].append((start, 1 / rate))
            max_amounts = defaultdict(lambda: 0)
            max_amounts[start_currency] = 1.0
            queue = deque([start_currency])
            while queue:
                current = queue.popleft()
                current_amount = max_amounts[current]
                for neighbor, rate in graph[current]:
                    new_amount = current_amount * rate
                    if new_amount > max_amounts[neighbor]:
                        max_amounts[neighbor] = new_amount
                        queue.append(neighbor)
            return max_amounts
        
        day1_results = bfs(initialCurrency, pairs1, rates1)
        max_final_amount = 0.0
        for currency in day1_results:
            after_day2_results = bfs(currency, pairs2, rates2)
            max_final_amount = max(max_final_amount, after_day2_results.get(initialCurrency, 0) * day1_results[currency])
        return max_final_amount
# @lc code=end