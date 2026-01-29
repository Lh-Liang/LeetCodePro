#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        # Sort edges by weight descending order
        edges.sort(key=lambda x: -x[2])
        
        # Initialize degree count for each node and union-find structure for connectivity check
        parent = list(range(len(edges) + 1))
        degree = defaultdict(int)
        total_weight = 0  # To store the sum of selected edge weights
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                return True
            return False
        
        for u, v, w in edges:
            # Ensure adding this edge will not create a cycle (connectivity check)
            if degree[u] < k and degree[v] < k and union(u, v):
                degree[u] += 1
                degree[v] += 1
                total_weight += w  # Add weight of this edge to total
        
        return total_weight
# @lc code=end