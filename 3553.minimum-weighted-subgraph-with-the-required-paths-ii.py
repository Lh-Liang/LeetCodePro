#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

import heapq
from typing import List

# @lc code=start
class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        # Build adjacency list for undirected graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(source):
            dist = [float('inf')] * n
            dist[source] = 0
            min_heap = [(0, source)]
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                if current_dist > dist[u]:
                    continue
                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(min_heap, (dist[v], v))
            return dist
        
        results = []
        for src1, src2, dest in queries:
            # Find shortest path distances from src1, src2 and dest
            dist_from_src1 = dijkstra(src1)
            dist_from_src2 = dijkstra(src2)
            dist_from_dest = dijkstra(dest)
            
            # Determine minimal subtree total weight for this query
            min_total_weight = float('inf')
            for node in range(n):
                if (dist_from_src1[node] < float('inf') and \
                    dist_from_src2[node] < float('inf') and \
                    dist_from_dest[node] < float('inf')):
                    total_weight = (dist_from_src1[node] + \
dist_from_src2[node] + \
dist_from_dest[node])
                    min_total_weight = min(min_total_weight, total_weight)
            results.append(min_total_weight if min_total_weight != float('inf') else -1)
        return results
# @lc code=end