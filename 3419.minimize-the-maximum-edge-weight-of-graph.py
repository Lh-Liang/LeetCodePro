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
        # Get all unique weights for binary search
        weights = sorted(set(e[2] for e in edges))
        
        if not weights:
            return -1
        
        def canReachAll(maxWeight):
            # Build reversed graph with edges <= maxWeight
            reversed_graph = defaultdict(list)
            for a, b, w in edges:
                if w <= maxWeight:
                    # Original: a -> b, Reversed: b -> a
                    reversed_graph[b].append(a)
            
            # BFS from node 0 in reversed graph
            visited = [False] * n
            visited[0] = True
            queue = deque([0])
            count = 1
            
            while queue:
                node = queue.popleft()
                for neighbor in reversed_graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        count += 1
                        queue.append(neighbor)
            
            return count == n
        
        # Binary search on weights
        left, right = 0, len(weights) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canReachAll(weights[mid]):
                result = weights[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return result
# @lc code=end