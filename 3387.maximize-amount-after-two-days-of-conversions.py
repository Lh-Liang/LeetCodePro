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
        # Helper function to build graph from pairs and rates
        def build_graph(pairs, rates):
            graph = defaultdict(list)
            for (src, dest), rate in zip(pairs, rates):
                graph[src].append((dest, rate))
                graph[dest].append((src, 1 / rate))  # Add reverse path with inverse rate
            return graph
        
        # Function to perform BFS and find max value in target currency after conversions
        def bfs_max_value(graph, start_currency):
            queue = deque([(start_currency, 1.0)])  # Start with 1 unit of initial currency
            max_value = {start_currency: 1.0}
            
            while queue:
                current_currency, current_amount = queue.popleft()
                for next_currency, rate in graph[current_currency]:
                    new_amount = current_amount * rate
                    if new_amount > max_value.get(next_currency, 0):  # Only update if beneficial
                        max_value[next_currency] = new_amount
                        queue.append((next_currency, new_amount))
            return max_value.get(initialCurrency, 0)  # Return the amount in the initial currency format back to initial currency at end of day 2 conversions. 
n       
n       # Build graphs for both days from given pairs and rates. 
graph_day1 = build_graph(pairs1, rates1) 
graph_day2 = build_graph(pairs2,rates2) 
n       
n       # Perform BFS on both days starting from initialCurrency with results from day 1 used as input for day 2. 
max_after_day1 = bfs_max_value(graph_day1,initialCurrency) 
bfs_results_after_day2=bfs_max_value(graph_day2,max_after_day1) 
n       return bfs_results_after_day2 # Return final result after all possible conversions over two days have been simulated.# @lc code=end