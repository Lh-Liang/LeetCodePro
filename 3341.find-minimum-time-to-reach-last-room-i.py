#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
from typing import List
import heapq
import math

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        dist = [[math.inf] * m for _ in range(n)]
        start_time = max(0, moveTime[0][0])
        dist[0][0] = start_time

        pq = [(start_time, 0, 0)]  # (time, r, c)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            t, r, c = heapq.heappop(pq)
            if t != dist[r][c]:
                continue
            if r == n - 1 and c == m - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    nt = max(t + 1, moveTime[nr][nc])
                    if nt < dist[nr][nc]:
                        dist[nr][nc] = nt
                        heapq.heappush(pq, (nt, nr, nc))

        return dist[n - 1][m - 1]
# @lc code=end
