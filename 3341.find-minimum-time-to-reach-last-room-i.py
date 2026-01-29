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
        n = len(moveTime)
        m = len(moveTime[0])
        
        # dist[r][c] stores the minimum time to reach room (r, c)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        # Priority queue stores (current_time, row, col)
        pq = [(0, 0, 0)]
        
        while pq:
            t, r, c = heapq.heappop(pq)
            
            # If we've already found a better path to this room, skip
            if t > dist[r][c]:
                continue
            
            # Target reached
            if r == n - 1 and c == m - 1:
                return t
            
            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    # Arrival time = max(current_time, open_time) + 1 second travel
                    new_time = max(t, moveTime[nr][nc]) + 1
                    
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(pq, (new_time, nr, nc))
        
        return -1
# @lc code=end