#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        
        # Priority queue stores tuples of (time, row, col)
        # Start at (0, 0) with time 0
        pq = [(0, 0, 0)]
        
        # Distance matrix to keep track of minimum time to reach each cell
        min_time = [[float('inf')] * m for _ in range(n)]
        min_time[0][0] = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            t, r, c = heapq.heappop(pq)
            
            # If we reached the destination
            if r == n - 1 and c == m - 1:
                return t
            
            # If we found a faster way to this cell already, skip
            if t > min_time[r][c]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    # The time to arrive at the next cell is:
                    # max(current_time, time_needed_for_next_cell_to_open) + 1 second to move
                    # We wait at current cell until moveTime[nr][nc] if necessary, 
                    # effectively leaving at max(t, moveTime[nr][nc])
                    new_time = max(t, moveTime[nr][nc]) + 1
                    
                    if new_time < min_time[nr][nc]:
                        min_time[nr][nc] = new_time
                        heapq.heappush(pq, (new_time, nr, nc))
                        
        return -1 # Should not be reached given constraints
# @lc code=end