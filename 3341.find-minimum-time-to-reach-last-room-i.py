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
        
        # Initialize distances with infinity and start point with 0
        # dist[i][j] stores the minimum time to reach room (i, j)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        # Priority queue stores (current_time, row, col)
        # We use a min-heap to always expand the node with the smallest time
        pq = [(0, 0, 0)]
        
        while pq:
            t, r, c = heapq.heappop(pq)
            
            # If we reached the destination, we can return immediately
            if r == n - 1 and c == m - 1:
                return t
            
            # Standard Dijkstra: if we found a better path to this cell already, skip
            if t > dist[r][c]:
                continue
            
            # Explore all 4 adjacent neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    # The room opens at moveTime[nr][nc]. 
                    # We can only move there at max(current_time, moveTime[nr][nc])
                    # and the move itself takes exactly 1 second.
                    arrival_time = max(t, moveTime[nr][nc]) + 1
                    
                    if arrival_time < dist[nr][nc]:
                        dist[nr][nc] = arrival_time
                        heapq.heappush(pq, (arrival_time, nr, nc))
        
        return dist[n-1][m-1]
# @lc code=end