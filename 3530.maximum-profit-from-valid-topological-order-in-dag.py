#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        from collections import deque, defaultdict
        # Step 1: Perform topological sort using Kahn's algorithm
        indegree = [0] * n
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            indegree[v] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 2: Assign positions based on scores to maximize profit while respecting the topological order.
        # Sort nodes by score descending within their topologically sorted group.
        position_multiplier = defaultdict(int)
        sorted_positions = range(1, n + 1)
        # Sort topo_order based on scores descending to maximize profit within valid orderings.
        sorted_topo_order = sorted(topo_order, key=lambda x: score[x], reverse=True)

        max_profit = 0
        for pos, node in zip(sorted_positions, sorted_topo_order):
            max_profit += pos * score[node]

        return max_profit
# @lc code=end