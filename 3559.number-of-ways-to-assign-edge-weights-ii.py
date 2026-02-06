#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
from typing import List, Dict
from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        # Step 1: Create an adjacency list for the graph representation of the tree.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Helper function to perform DFS and find path from start to end node.
        def find_path(start: int, end: int) -> List[int]:
            stack = [(start, [start])]
            visited = set()
            while stack:
                node, path = stack.pop()
                if node == end:
                    return path
                if node not in visited:
                    visited.add(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append((neighbor, path + [neighbor]))
            return []  # Should never reach here if input is valid as per constraints.
        
        def calculate_odd_cost_ways(path_length: int) -> int:
            # Calculate number of ways such that sum of weights is odd.
            if path_length == 0:
                return 0
            # If there are k edges in the path, odd weight sum occurs when there are an odd number of '1's.
            total_ways = pow(2, path_length - 1, MOD) # Any one edge out of k can be '1' while others '2'
            return total_ways % MOD
        
        answers = []
        for u, v in queries:
            path = find_path(u, v)											# Step 2: Find path using DFS
            num_edges_in_path = len(path) - 1                 # Step 3: Calculate number of edges on this path
            answers.append(calculate_odd_cost_ways(num_edges_in_path))	# Step 4 & Step 5
        return answers
# @lc code=end