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
        graph = [[] for _ in range(n)]
        for u, v, start, end in edges:
            graph[u].append((v, start, end))
        min_time = [float('inf')] * n
        min_time[0] = 0
        pq = [(0, 0)]  # (time, node)
        while pq:
            curr_time, u = heapq.heappop(pq)
            if u == n - 1:
                return curr_time
            if curr_time > min_time[u]:
                continue
            for v, start, end in graph[u]:
                wait_time = max(0, start - curr_time) if curr_time <= end else float('inf')
                new_time = curr_time + wait_time + 1  # travel takes one unit time
                if new_time < min_time[v]:
                    min_time[v] = new_time
                    heapq.heappush(pq, (new_time, v))
        return -1  # unreachable case if while loop ends without return statement. # @lc code=end