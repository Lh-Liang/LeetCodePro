#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        import heapq
        from collections import defaultdict
        # Create adjacency list for graph
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))

        # Priority queue for Dijkstra's algorithm (time, node)
        pq = [(0, 0)] # Start at node 0 at time 0
        # Dictionary to store minimum time to reach each node
        min_time = {i: float('inf') for i in range(n)}
        min_time[0] = 0
        
        while pq:
            current_time, node = heapq.heappop(pq)
            if node == n - 1:
                return current_time # Reached destination node n-1
            if current_time > min_time[node]:
                continue # Skip if we have already found a better time
            for neighbor, start, end in graph[node]:
                wait_time = max(0, start - current_time) # Wait if needed until edge is available
                arrival_time = current_time + wait_time + 1 # One unit of time to travel the edge
                if start <= arrival_time <= end and arrival_time < min_time[neighbor]:
                    min_time[neighbor] = arrival_time
                    heapq.heappush(pq, (arrival_time, neighbor)) # Push new state into priority queue 
        return -1 # If no path found to node n-1
# @lc code=end