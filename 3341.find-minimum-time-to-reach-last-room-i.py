#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        # Dijkstra's algorithm: (time, row, col)
        # time is the current time we reach (row, col)
        # We start at (0,0) at time 0
        heap = [(0, 0, 0)]
        # visited matrix with minimum time to reach each cell
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while heap:
            t, i, j = heapq.heappop(heap)
            if i == n-1 and j == m-1:
                return t
            if t > visited[i][j]:
                continue
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    # The earliest time we can enter (ni,nj) is max(t+1, moveTime[ni][nj])
                    # because moving takes 1 second and the room opens at moveTime[ni][nj]
                    nt = max(t + 1, moveTime[ni][nj])
                    if nt < visited[ni][nj]:
                        visited[ni][nj] = nt
                        heapq.heappush(heap, (nt, ni, nj))
        return visited[n-1][m-1]
# @lc code=end