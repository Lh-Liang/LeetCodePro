#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        from heapq import heappop, heappush
        import collections
        
        # Create adjacency list with edge availability
        graph = collections.defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))
        
        # Priority queue (min-heap) and times dictionary
        pq = [(0, 0)]  # (current_time, node)
        times = {i: float('inf') for i in range(n)}
        times[0] = 0  # Start at node 0 at time 0
        
        while pq:
            current_time, u = heappop(pq)
            if u == n - 1:
                return current_time  # Return if reached destination node n-1
            # Explore neighbors of u
            for v, start, end in graph[u]:
                wait_time = max(start - current_time, 0)
                arrival_time = current_time + wait_time + 1  # move takes 1 unit time
                if arrival_time <= end and arrival_time < times[v]:
                    times[v] = arrival_time
                    heappush(pq, (arrival_time, v))
        return -1  # If destination is never reached
# @lc code=end