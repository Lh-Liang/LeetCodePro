#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class Solution:
    MOD = 10**9 + 7
    
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Build adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Function to perform DFS and find path from source to target
        def find_path(source, target):
            stack = [(source, [source])]
            visited = set()
            while stack:
                node, path = stack.pop()
                if node == target:
                    return path
                if node not in visited:
                    visited.add(node)
                    for neighbor in tree[node]:
                        if neighbor not in visited:
                            stack.append((neighbor, path + [neighbor]))
            return []
        
        # Calculate number of ways to assign weights such that cost is odd
        def count_odd_weight_assignments(path_length):
            # We need an odd number of edges with weight 1
            return pow(2, path_length - 1, self.MOD)
        
        results = []
        for u, v in queries:
            path = find_path(u, v)
            if not path or len(path) < 2:
                results.append(0)
                continue
            # Number of edges is path length - 1
            num_edges = len(path) - 1
            results.append(count_odd_weight_assignments(num_edges))
        
        return results
# @lc code=end