#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, start, end in edges:
            adj[u].append((v, start, end))
        
        # Dijkstra-like algorithm with time constraints
        # dist[i] = earliest arrival time at node i
        INF = 10**18
        dist = [INF] * n
        dist[0] = 0  # start at node 0 at time 0
        
        # priority queue: (current_time, node)
        pq = [(0, 0)]  # (time, node)
        
        while pq:
            t, u = heapq.heappop(pq)
            if t > dist[u]:
                continue
            if u == n - 1:
                return t  # first time we pop destination is minimal
            
            # Explore outgoing edges from u
            for v, start, end in adj[u]:
                # If we can take this edge: need start <= current_time <= end?
                # Actually we can wait at u until start time if needed.
                # The earliest we can depart from u to take this edge is max(t, start).
                depart_time = max(t, start)
                if depart_time <= end:
                    arrival_time = depart_time + 1  # travel takes 1 unit
                    if arrival_time < dist[v]:
                        dist[v] = arrival_time
                        heapq.heappush(pq, (arrival_time, v))
            
            # We don't explicitly wait beyond exploring edges because waiting is handled by depart_time = max(t, start).
            # However we might need to wait even if there are no edges? But we only push when we take an edge.
            # But waiting indefinitely without taking an edge is useless.
            # So the algorithm is correct.
        
        return -1 if dist[n-1] == INF else dist[n-1]
# @lc code=end