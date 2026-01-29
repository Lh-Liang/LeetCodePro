#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

from heapq import heappop, heappush
from collections import defaultdict
import sys

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list for graph representation
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))
        
        # Min heap for Dijkstra's algorithm (time, node)
        pq = [(0, 0)]
        # Array to track minimum time to reach each node,
        # initialized with infinity
        min_time = [sys.maxsize] * n
        min_time[0] = 0
        
        while pq:
            curr_time, u = heappop(pq)
            # Check if we have reached the last node
            if u == n - 1:
                return curr_time
            
            # Explore all outgoing edges from current node u
            for v, start, end in graph[u]:
                # Wait until within valid travel time window if necessary
                next_time = max(curr_time + 1, start)
                if next_time <= end and next_time < min_time[v]:
                    min_time[v] = next_time
                    heappush(pq, (next_time, v))
                    
        return -1
# @lc code=end