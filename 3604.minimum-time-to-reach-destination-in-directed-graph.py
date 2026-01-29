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
        # Build adjacency list: u -> list of (v, start_time, end_time)
        adj = [[] for _ in range(n)]
        for u, v, s, e in edges:
            adj[u].append((v, s, e))
        
        # dist[i] stores the earliest arrival time at node i
        dist = [float('inf')] * n
        dist[0] = 0
        
        # Priority queue: (arrival_time, current_node)
        pq = [(0, 0)]
        
        while pq:
            t, u = heapq.heappop(pq)
            
            # Standard Dijkstra pruning
            if t > dist[u]:
                continue
            
            # Goal check
            if u == n - 1:
                return t
            
            for v, s, e in adj[u]:
                # Earliest time we can depart from u using this edge
                # We either depart immediately (t) or wait until it opens (s)
                departure_time = max(t, s)
                
                # Check if the edge is still valid at the earliest departure time
                if departure_time <= e:
                    # Arrival at v is 1 unit of time after departure
                    arrival_v = departure_time + 1
                    if arrival_v < dist[v]:
                        dist[v] = arrival_v
                        heapq.heappush(pq, (arrival_v, v))
        
        return -1
# @lc code=end