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
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # right, down, left, up
        pq = [(0, 0, 0)]  # (time, x, y)
        visited = set()
        while pq:
            t, x, y = heappop(pq)
            if (x, y) == (n - 1, m - 1):
                return t
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    wait_time = max(0, moveTime[nx][ny] - t - 1)
                    heappush(pq, (t + wait_time + 1, nx, ny))
        return -1   # If unreachable which theoretically shouldn't happen based on constraints.
# @lc code=end