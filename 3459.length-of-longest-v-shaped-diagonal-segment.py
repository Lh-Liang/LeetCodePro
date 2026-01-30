#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_length = 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        def dfs(x, y, dx, dy, length):
            if x < 0 or x >= n or y < 0 or y >= m:
                return length
            if length % 2 == 0 and grid[x][y] != 2:
                return length
            if length % 2 == 1 and grid[x][y] != 0:
                return length
            return dfs(x + dx, y + dy, dx, dy, length + 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in directions:
                        max_length = max(max_length, dfs(i + d[0], j + d[1], d[0], d[1], 2))
        return max_length
# @lc code=end