#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        def build_graph(edges):
            graph = defaultdict(list)
            for u, v, w in edges:
                graph[u].append((v, w))
                graph[v].append((u, w))
            return graph
        
        def bfs(source):
            dist = {i: float('inf') for i in range(n)}
            queue = deque([(source, 0)])
            dist[source] = 0
            while queue:
                node, curr_dist = queue.popleft()
                for neighbor, weight in graph[node]:
                    if curr_dist + weight < dist[neighbor]:
                        dist[neighbor] = curr_dist + weight
                        queue.append((neighbor, dist[neighbor]))
            return dist
        
        n = len(edges) + 1  # since it's a tree with n nodes and n-1 edges
        graph = build_graph(edges)
        results = []
        
        for src1, src2, dest in queries:
            dist_from_src1 = bfs(src1)
            dist_from_src2 = bfs(src2)
            dist_from_dest = bfs(dest)
            
            min_weight = float('inf')
            for i in range(n):
                # Check if node i can be an intersection point such that src1 -> i -> dest and src2 -> i -> dest are valid paths.
                if dist_from_src1[i] != float('inf') and dist_from_src2[i] != float('inf') and dist_from_dest[i] != float('inf'):
                    total_weight = dist_from_src1[i] + dist_from_src2[i] + dist_from_dest[i]
                    min_weight = min(min_weight, total_weight)
            results.append(min_weight if min_weight != float('inf') else -1)
        return results
# @lc code=end