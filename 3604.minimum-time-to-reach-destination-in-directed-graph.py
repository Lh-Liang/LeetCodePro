#
# @lc app=leetcode id=3604 lang=python3
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

from typing import List
import heapq

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0

        g = [[] for _ in range(n)]
        for u, v, s, e in edges:
            g[u].append((v, s, e))

        INF = 10**30
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (time, node)

        while pq:
            t, u = heapq.heappop(pq)
            if t != dist[u]:
                continue
            if u == n - 1:
                return t

            for v, s, e in g[u]:
                if t > e:
                    continue
                depart = s if t < s else t
                nt = depart + 1
                if nt < dist[v]:
                    dist[v] = nt
                    heapq.heappush(pq, (nt, v))

        return -1
# @lc code=end
