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
        INF = 10**18
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # time, r, c
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while pq:
            time, r, c = heapq.heappop(pq)
            if time > dist[r][c]:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    new_time = max(time, moveTime[nr][nc]) + 1
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(pq, (new_time, nr, nc))
        return dist[n - 1][m - 1]

# @lc code=end