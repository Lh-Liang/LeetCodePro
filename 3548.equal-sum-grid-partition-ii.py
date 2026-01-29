#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def is_connected(grid_section):
            m, n = len(grid_section), len(grid_section[0])
            visited = set()
            stack = [(0, 0)]
            visited.add((0, 0))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            connected_cells = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid_section[nx][ny] != -1:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        connected_cells += 1
            return connected_cells == m * n - 1
        
        m = len(grid)
        n = len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        
        for r in range(1, m):  # Horizontal cuts
            top_sum = sum(sum(row) for row in grid[:r])
            bottom_sum = total_sum - top_sum
            if top_sum == bottom_sum:
                return True
            # Check by discounting one cell from either top or bottom part and checking connectivity
            for c in range(n):
                new_top_sum = top_sum - grid[r-1][c]
                new_bottom_sum = bottom_sum - grid[r][c]
                if new_top_sum == new_bottom_sum:
                    if is_connected([row[:c] + row[c+1:] for row in grid[:r]]) or \
is_connected([row[:c] + row[c+1:] for row in grid[r:]]):"]                      return True
        \\[vertical cut logic similar]\/"]";\""]          "}\u000a \u000a     "#: @lc code=end"\u000a "