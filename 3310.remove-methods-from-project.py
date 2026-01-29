#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
from typing import List, Set, Dict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build graph using adjacency list and reverse graph for checking incoming edges
        graph = {i: [] for i in range(n)}
        reverse_graph = {i: [] for i in range(n)}
        for a, b in invocations:
            graph[a].append(b)
            reverse_graph[b].append(a)
        
        # Step 2: Identify all suspicious methods using DFS starting from k
        suspicious_methods = set()
        def dfs(node):
            if node not in suspicious_methods:
                suspicious_methods.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)
        dfs(k)
        
        # Step 3: Check if any external invocation exists pointing into the suspicious group
        for method in suspicious_methods:
            for invoker in reverse_graph[method]:
                if invoker not in suspicious_methods:
                    return list(range(n))  # Suspicious group cannot be safely removed
        
        # Step 4: If no external invocations exist, remove suspicious methods and return remaining ones
        return [i for i in range(n) if i not in suspicious_methods]
# @lc code=end