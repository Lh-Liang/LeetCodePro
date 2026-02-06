#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        import heapq
        
        def dijkstra(start):
            dist = {i: float('inf') for i in range(n)}
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                curr_dist, u = heapq.heappop(heap)
                if curr_dist > dist[u]:
                    continue
                for v, weight in graph[u]:
                    if dist[v] > curr_dist + weight:
                        dist[v] = curr_dist + weight
                        heapq.heappush(heap, (dist[v], v))
            return dist
        
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w)) # since it's an undirected tree
        
        results = []
        for src1, src2, dest in queries:
            dist_from_src1 = dijkstra(src1)
            dist_from_src2 = dijkstra(src2)
            min_weight = float('inf')
            for node in range(n):
                if node in [src1, src2]:
                    continue
                if dist_from_src1[node] != float('inf') and dist_from_src2[node] != float('inf'):
                    min_weight = min(min_weight, dist_from_src1[node] + dist_from_src2[node])
            result_weight = min_weight + (dist_from_src1[dest] if dest in dist_from_src1 else float('inf')) + (dist_from_src2[dest] if dest in dist_from_src2 else float('inf')) - min_weight # corrects double counting dest path weight once
            results.append(result_weight if result_weight != float('inf') else -1)
        return results
# @lc code=end