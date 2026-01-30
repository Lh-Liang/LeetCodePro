#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
from heapq import heappop, heappush
from collections import defaultdict
import sys
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        # Create graph adjacency list with constraints on when an edge can be used.
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))
        
        # Priority queue for Dijkstra's algorithm (min-heap based on current time to reach a node)
        pq = [(0, 0)] # (current_time, current_node)
        
        # Dictionary to store minimum times to reach each node.
        min_time = {i: sys.maxsize for i in range(n)}
        min_time[0] = 0
        
        while pq:
            current_time, u = heappop(pq)
            
            # If we have reached node n-1 with minimum time.
            if u == n - 1:
                return current_time
            
            # Traverse all edges from current node u.
            for v, start_time, end_time in graph[u]:
                # Wait until we can use this edge if necessary.
                if current_time < start_time:
                    wait_time = start_time - current_time
                else:
                    wait_time = 0
                
                new_time = current_time + wait_time + 1 # +1 since it takes one unit of time to traverse an edge.
                
                if new_time < min_time[v] and new_time <= end_time:
                    min_time[v] = new_time
                    heappush(pq, (new_time, v))
        
        return -1 # Impossible to reach n-1 if we've exhausted all paths without success.
# @lc code=end