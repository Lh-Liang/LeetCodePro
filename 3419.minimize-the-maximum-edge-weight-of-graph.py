#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Step 1: Sort edges based on weights for binary search purposes.
        edges.sort(key=lambda x: x[2])
        
        # Helper function to check if node 0 is reachable from all nodes within weight limit and threshold.
        def canReachZero(max_weight):
            graph = defaultdict(list)
            for u, v, w in edges:
                if w <= max_weight:
                    graph[u].append((v, w))
            
            # Use BFS or DFS to check reachability from all nodes to node 0 with threshold constraint.
            visited = set()
            def bfs(start):
                queue = deque([start])
                visited.add(start)
                while queue:
                    node = queue.popleft()
                    for neighbor, weight in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            
            bfs(0)  # Start BFS from node 0.
            return len(visited) == n  # Check if all nodes are reachable to node 0. 
        
        # Step 2: Perform binary search on the sorted edge weights.
        low, high = 0, len(edges) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if canReachZero(edges[mid][2]): # Check reachability with current mid as max weight.
                result = edges[mid][2]& high = mid - 1 & update result with lower weight. & else: low = mid + 1 # Increase lower bound if not reachable. & return result