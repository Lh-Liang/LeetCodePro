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
        # Create adjacency list for the directed graph
        adj = [[] for _ in range(n)]
        for u, v, s, e in edges:
            adj[u].append((v, s, e))
        
        # Priority queue stores (current_time, current_node)
        pq = [(0, 0)]
        # min_time[i] stores the earliest time we can reach node i
        min_time = [float('inf')] * n
        min_time[0] = 0
        
        while pq:
            t, u = heapq.heappop(pq)
            
            # If we reached the destination node, return the time
            if u == n - 1:
                return t
            
            # If we've already found a faster way to reach this node, skip
            if t > min_time[u]:
                continue
            
            for v, s, e in adj[u]:
                # The earliest time we can start moving on this edge is max(arrival_time, start_time)
                start_travel_time = max(t, s)
                
                # Can only use the edge if the starting time is within [start_time, end_time]
                if start_travel_time <= e:
                    # Arrival time at the next node is travel_start_time + 1
                    arrival_time = start_travel_time + 1
                    
                    # If this path is faster, update min_time and add to priority queue
                    if arrival_time < min_time[v]:
                        min_time[v] = arrival_time
                        heapq.heappush(pq, (arrival_time, v))
        
        # If node n-1 is not reachable
        return -1
# @lc code=end