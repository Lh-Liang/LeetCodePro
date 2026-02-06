#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        from heapq import heappop, heappush
        n, m = len(moveTime), len(moveTime[0])
        pq = [(0, 0, 0)]  # (current_time, row, col)
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while pq:
            curr_time, x, y = heappop(pq)
            if (x, y) == (n - 1, m - 1):
                return curr_time
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    wait_time = max(0, moveTime[nx][ny] - (curr_time + 1))
                    heappush(pq, (curr_time + 1 + wait_time, nx, ny))
        return -1  # Just in case there is no path though constraints guarantee there is one.
# @lc code=end