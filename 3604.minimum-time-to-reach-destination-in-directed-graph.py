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
        # Adjacency list to store edges: node -> [(neighbor, start, end)]
        adj = [[] for _ in range(n)]
        for u, v, s, e in edges:
            adj[u].append((v, s, e))
        
        # Standard Dijkstra's algorithm to find the minimum time to reach each node
        # dist[i] will store the earliest time we can reach node i
        dist = [float('inf')] * n
        dist[0] = 0
        
        # Priority queue stores (time, current_node)
        pq = [(0, 0)]
        
        while pq:
            t, u = heapq.heappop(pq)
            
            # If we found a shorter path to u already, skip this
            if t > dist[u]:
                continue
            
            # If we reached the destination node, return the time
            if u == n - 1:
                return t
            
            for v, s, e in adj[u]:
                # To use edge (u, v) with window [s, e], we must be at u at some time T
                # such that s <= T <= e. Since we are at u at time t, the earliest
                # we can use the edge is at time T = max(t, s).
                start_time = max(t, s)
                
                # If the earliest possible start time is within the window [s, e]
                if start_time <= e:
                    # We arrive at node v at time T + 1
                    arrival_time = start_time + 1
                    if arrival_time < dist[v]:
                        dist[v] = arrival_time
                        heapq.heappush(pq, (arrival_time, v))
        
        # If the destination node is unreachable
        return -1
# @lc code=end