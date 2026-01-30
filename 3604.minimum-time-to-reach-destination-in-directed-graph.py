#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))

        INF = float('inf')
        # Track the earliest arrival time at each node
        arrival = [INF] * n
        arrival[0] = 0
        # Min-heap: (current_time, node)
        heap = [(0, 0)]
        while heap:
            t, u = heapq.heappop(heap)
            if u == n - 1:
                return t
            if t > arrival[u]:
                continue
            # Try all outgoing edges
            for v, start, end in graph[u]:
                # Wait until max(start, t)
                depart = max(start, t)
                if depart > end:
                    continue
                arrive = depart + 1
                if arrival[v] > arrive:
                    arrival[v] = arrive
                    heapq.heappush(heap, (arrive, v))
        return -1
# @lc code=end