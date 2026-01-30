#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
from heapq import heappop, heappush
from collections import defaultdict
from typing import List

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Union-Find helper methods
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]
        
        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                    
        # Initialize union-find structures and other variables
        parent = list(range(n))
        rank = [0] * n
        max_edge_weight = -1
        # Priority queue for sorting edges by weight (min-heap)
        pq = []
        for u, v, w in edges:
            heappush(pq, (w, u, v))
            
        # Track number of outgoing edges per node 
        out_degree = defaultdict(int)
        
        # Process edges by increasing weight using priority queue
        while pq:
            w, u, v = heappop(pq)
            if out_degree[u] < threshold and out_degree[v] < threshold:
                # Check if adding this edge maintains connectivity using union-find
                if find(parent, u) != find(parent, v):
                    union(parent, rank, u, v)
                    max_edge_weight = max(max_edge_weight, w)
                    out_degree[u] += 1
                    out_degree[v] += 1
                    
        # Verify all nodes are reachable from node 0; else return -1.
        for i in range(n):
            if find(parent, i) != find(parent, 0):
                return -1
                
        return max_edge_weight if max_edge_weight != -1 else -1
# @lc code=end