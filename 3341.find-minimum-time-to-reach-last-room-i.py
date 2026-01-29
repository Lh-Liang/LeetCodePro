#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        # dist[i][j] stores the minimum time to reach room (i, j)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        # Priority queue stores (time, row, col)
        pq = [(0, 0, 0)]
        
        while pq:
            t, r, c = heapq.heappop(pq)
            
            if t > dist[r][c]:
                continue
            
            if r == n - 1 and c == m - 1:
                return t
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    # Arrival time is the max of current time and opening time, plus 1s travel
                    arrival_time = max(t, moveTime[nr][nc]) + 1
                    if arrival_time < dist[nr][nc]:
                        dist[nr][nc] = arrival_time
                        heapq.heappush(pq, (arrival_time, nr, nc))
        
        return -1
# @lc code=end