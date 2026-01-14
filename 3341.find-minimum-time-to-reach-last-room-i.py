#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#
# @lc code=start
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        # dist[i][j] = minimum time to reach room (i, j)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        # Min heap: (time, row, col)
        heap = [(0, 0, 0)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while heap:
            time, r, c = heapq.heappop(heap)
            
            # If we've already found a better path, skip
            if time > dist[r][c]:
                continue
            
            # If we've reached the destination
            if r == n - 1 and c == m - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    # Calculate arrival time at (nr, nc)
                    # We can start moving when time >= moveTime[nr][nc]
                    arrival = max(time, moveTime[nr][nc]) + 1
                    
                    if arrival < dist[nr][nc]:
                        dist[nr][nc] = arrival
                        heapq.heappush(heap, (arrival, nr, nc))
        
        return dist[n-1][m-1]
# @lc code=end