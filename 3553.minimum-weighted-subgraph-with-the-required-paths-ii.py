#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#
# @lc code=start
class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import deque
        
        n = len(edges) + 1
        
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Compute distances from a given start node to all other nodes
        def compute_distances(start):
            dist = [float('inf')] * n
            dist[start] = 0
            queue = deque([start])
            
            while queue:
                u = queue.popleft()
                for v, w in graph[u]:
                    if dist[v] == float('inf'):
                        dist[v] = dist[u] + w
                        queue.append(v)
            
            return dist
        
        # Precompute distances from all nodes
        all_distances = [compute_distances(i) for i in range(n)]
        
        # Process each query
        result = []
        for src1, src2, dest in queries:
            min_weight = float('inf')
            # Try each node as the meeting point
            for meet in range(n):
                weight = (all_distances[src1][meet] + 
                         all_distances[src2][meet] + 
                         all_distances[meet][dest])
                min_weight = min(min_weight, weight)
            result.append(int(min_weight))
        
        return result
# @lc code=end