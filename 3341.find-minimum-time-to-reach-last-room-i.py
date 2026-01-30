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
        # Initialize the min time matrix with infinity
        min_time = [[float('inf')] * m for _ in range(n)]
        min_time[0][0] = 0
        # Priority queue: (current_time, i, j)
        heap = [(0, 0, 0)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while heap:
            t, x, y = heapq.heappop(heap)
            if (x, y) == (n-1, m-1):
                return t
            if t > min_time[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    next_time = max(t + 1, moveTime[nx][ny])
                    if next_time < min_time[nx][ny]:
                        min_time[nx][ny] = next_time
                        heapq.heappush(heap, (next_time, nx, ny))
        return -1  # unreachable
# @lc code=end