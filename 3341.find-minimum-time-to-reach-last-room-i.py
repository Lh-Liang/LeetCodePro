#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
from heapq import heappop, heappush
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        visited = set()
        # Min-heap priority queue initialized with starting point at zero time
        pq = [(0, 0, 0)] # (time, x, y)
        while pq:
            time, x, y = heappop(pq)
            if (x, y) == (n-1, m-1): # Reached destination room
                return time
            if (x, y) in visited:
                continue    
            visited.add((x,y))    
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    # Calculate wait time if needed before moving to next room. 
                    next_time = max(time + 1 , moveTime[nx][ny]) 
                    heappush(pq,(next_time,nx , ny))
        return -1 # If no path is found which shouldn't happen as per constraints. 
# @lc code=end