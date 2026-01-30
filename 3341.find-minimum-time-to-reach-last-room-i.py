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
        n, m = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0)]  # (time, x, y)
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while heap:
            t, x, y = heapq.heappop(heap)
            if (x, y) == (n-1, m-1):
                return t
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nt = max(t + 1, moveTime[nx][ny])
                    if nt < visited[nx][ny]:
                        visited[nx][ny] = nt
                        heapq.heappush(heap, (nt, nx, ny))
        return -1
# @lc code=end