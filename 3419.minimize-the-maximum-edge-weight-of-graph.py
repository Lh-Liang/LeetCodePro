#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
from typing import List
from collections import defaultdict, deque
import heapq

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def canReachAllNodes(maxWeight):
            graph = defaultdict(list)
            for u, v, w in edges:
                if w <= maxWeight:
                    graph[u].append((v, w))
            
            visited = set()
            queue = deque([0])
            visited.add(0)
            while queue:
                node = queue.popleft()
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited) == n
        
        def validWithThreshold(maxWeight):
            outDegrees = defaultdict(list)
            for u, v, w in edges:
                if w <= maxWeight:
                    heapq.heappush(outDegrees[u], (-w, v))
                    if len(outDegrees[u]) > threshold:
                        heapq.heappop(outDegrees[u])
            return all(len(outDegrees[u]) <= threshold for u in range(n))
        
        left, right = 1, max(w for _, _, w in edges)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if canReachAllNodes(mid) and validWithThreshold(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
# @lc code=end