#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        from collections import defaultdict, deque
        # Step 1: Build graph and compute in-degrees of each node
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Step 2: Perform topological sort using Kahn's algorithm
        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Calculate maximum profit by assigning position optimally based on scores
        topo_order.sort(key=lambda x: score[x], reverse=True)  # Sort topo order by score desc. 
        max_profit = sum(score[node] * (i + 1) for i, node in enumerate(topo_order))
        return max_profit
# @lc code=end