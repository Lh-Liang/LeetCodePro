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
        rows, cols = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        pq = [(0, 0, 0)] # (time, row, col)
        visited = set()
        min_time = [[float('inf')] * cols for _ in range(rows)]
        min_time[0][0] = 0
        
        while pq:
            current_time, x, y = heappop(pq)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if x == rows - 1 and y == cols - 1:
                return current_time
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    wait_time = max(moveTime[nx][ny] - current_time - 1, 0)
                    new_time = current_time + wait_time + 1
                    if new_time < min_time[nx][ny]:
                        min_time[nx][ny] = new_time
                        heappush(pq, (new_time, nx, ny))
        return -1 # If unreachable under constraints logic.
# @lc code=end