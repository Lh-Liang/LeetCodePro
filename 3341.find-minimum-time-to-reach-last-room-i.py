#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        import heapq
        
        n = len(moveTime)
        m = len(moveTime[0])
        
        # Priority queue: (time, row, col)
        pq = [(0, 0, 0)]
        # Visited array to store minimum time to reach each cell
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            time, x, y = heapq.heappop(pq)
            
            # If we reached the destination
            if x == n - 1 and y == m - 1:
                return time
            
            # If we have already found a better path to this cell
            if time > dist[x][y]:
                continue
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check bounds
                if 0 <= nx < n and 0 <= ny < m:
                    # Time to move to the neighbor cell
                    # We need to wait until moveTime[nx][ny] to enter the room
                    # And it takes 1 second to move
                    new_time = max(time + 1, moveTime[nx][ny])
                    
                    # If we found a better path
                    if new_time < dist[nx][ny]:
                        dist[nx][ny] = new_time
                        heapq.heappush(pq, (new_time, nx, ny))
        
        return -1  # Should never reach here for valid inputs
# @lc code=end