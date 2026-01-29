#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
from typing import List
from collections import defaultdict, deque
from itertools import permutations

class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # Create adjacency list and indegree array
        adj_list = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj_list[u].append(v)
            indegree[v] += 1
        
        # Perform topological sort using Kahn's algorithm to get initial order candidates
        zero_indegree_queue = deque(i for i in range(n) if indegree[i] == 0)
        topological_order = []
        while zero_indegree_queue:
            node = zero_indegree_queue.popleft()
            topological_order.append(node)
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)
        
        # Explore all permutations of the topological order to find maximum profit
        max_profit = 0
        for perm in permutations(topological_order):
            current_profit = sum((pos + 1) * score[node] for pos, node in enumerate(perm))
            max_profit = max(max_profit, current_profit)
        
        return max_profit  # Return the highest profit found across all permutations.
# @lc code=end