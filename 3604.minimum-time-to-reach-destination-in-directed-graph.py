#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, start, end in edges:
            adj[u].append((v, start, end))
        
        # dist[i] stores the minimum time to reach node i
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]  # (time, node)
        
        while pq:
            t, u = heapq.heappop(pq)
            
            # If we reached the destination, return the time immediately
            if u == n - 1:
                return t
            
            # Standard Dijkstra pruning
            if t > dist[u]:
                continue
            
            for v, start, end in adj[u]:
                # Earliest time we can start traveling on this edge
                # is the arrival time at u or the start of the window, whichever is later.
                t_start = max(t, start)
                
                # Check if the earliest start time is within the edge's availability window
                if t_start <= end:
                    t_arrival = t_start + 1
                    if t_arrival < dist[v]:
                        dist[v] = t_arrival
                        heapq.heappush(pq, (t_arrival, v))
        
        return -1
# @lc code=end