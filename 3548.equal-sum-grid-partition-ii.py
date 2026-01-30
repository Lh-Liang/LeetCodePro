#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        # Try horizontal cuts
        row_sums = [sum(row) for row in grid]
        prefix_row = [0]*(m+1)
        for i in range(m):
            prefix_row[i+1] = prefix_row[i] + row_sums[i]
        for cut in range(1, m):  # cut after row cut-1
            top = prefix_row[cut]
            bottom = total - top
            if top == bottom:
                return True
            # Try to discount one cell from either section
            diff = abs(top-bottom)
            # Check top section (rows 0..cut-1)
            if top > bottom:
                for i in range(cut):
                    for j in range(n):
                        if top - grid[i][j] == bottom:
                            if self._is_connected_after_removal(grid, 0, 0, cut, n, i, j):
                                return True
            else:
                for i in range(cut, m):
                    for j in range(n):
                        if bottom - grid[i][j] == top:
                            if self._is_connected_after_removal(grid, cut, 0, m, n, i, j):
                                return True
        # Try vertical cuts
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        prefix_col = [0]*(n+1)
        for j in range(n):
            prefix_col[j+1] = prefix_col[j] + col_sums[j]
        for cut in range(1, n):  # cut after column cut-1
            left = prefix_col[cut]
            right = total - left
            if left == right:
                return True
            # Try to discount one cell from either section
            if left > right:
                for i in range(m):
                    for j in range(cut):
                        if left - grid[i][j] == right:
                            if self._is_connected_after_removal(grid, 0, 0, m, cut, i, j):
                                return True
            else:
                for i in range(m):
                    for j in range(cut, n):
                        if right - grid[i][j] == left:
                            if self._is_connected_after_removal(grid, 0, cut, m, n, i, j):
                                return True
        return False

    def _is_connected_after_removal(self, grid, row0, col0, row1, col1, remove_i, remove_j):
        # Returns True if the subgrid grid[row0:row1][col0:col1] is connected after removing (remove_i, remove_j)
        from collections import deque
        m, n = row1-row0, col1-col0
        visited = [[False]*n for _ in range(m)]
        # Mark removed cell as visited
        visited[remove_i-row0][remove_j-col0] = True
        # Find a starting cell (not removed)
        found = False
        for i in range(row0, row1):
            for j in range(col0, col1):
                if not (i == remove_i and j == remove_j):
                    start = (i, j)
                    found = True
                    break
            if found:
                break
        if not found:
            return False  # No cells to check
        # BFS
        q = deque()
        q.append((start[0]-row0, start[1]-col0))
        visited[start[0]-row0][start[1]-col0] = True
        count = 1
        total = (row1-row0)*(col1-col0)-1
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    count+=1
        return count == total
# @lc code=end