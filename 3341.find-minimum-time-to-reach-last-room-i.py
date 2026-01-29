#
# @lc app=leetcode id=3341 lang=python3
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        import heapq
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pq = [(0, 0, 0)]  # (time, x, y)
        visited = set()
        while pq:
            time, x, y = heapq.heappop(pq)
            if (x, y) == (n - 1, m - 1):
                return time
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    wait_time = max(0, moveTime[nx][ny] - (time + 1))
                    heapq.heappush(pq, (time + 1 + wait_time, nx, ny))
        return -1 # In case there's no path which shouldn't happen given constraints.
# @lc code=end