#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0]) if grid else 0
        
        # Helper function to check connectivity using BFS/DFS
        def is_connected(section):
            queue = [section[0]]
            visited = set(section[0])
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in section and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return len(visited) == len(section)
        
        # Calculate total sum of all elements in the grid
        total_sum = sum(sum(row) for row in grid)
        
        # Calculate prefix sums for rows and columns
        row_prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        col_prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(m):
            for j in range(n):
                row_prefix_sum[i+1][j+1] = row_prefix_sum[i+1][j] + grid[i][j]
                col_prefix_sum[j+1][i+1] = col_prefix_sum[j+1][i] + grid[i][j]
        
        max_cell_value = max(max(row) for row in grid)
        
        # Try horizontal cuts
        for i in range(1, m):
            top_half = sum(row_prefix_sum[k][-1] for k in range(0, i))
            bottom_half = total_sum - top_half
            if abs(top_half - bottom_half) <= max_cell_value:
                # Check connectivity after discounting logic is applied
                if is_connected({(x,y) for x in range(i) for y in range(n)}) and is_connected({(x,y) for x in range(i,m) for y in range(n)}):
                    return True
            
        # Try vertical cuts
        for j in range(1, n):
            left_half = sum(col_prefix_sum[k][-1] for k in range(0, j))
            right_half = total_sum - left_half
            if abs(left_half - right_half) <= max_cell_value:
                # Check connectivity after discounting logic is applied
                if is_connected({(x,y) for x in range(m) for y in range(j)}) and is_connected({(x,y) for x in range(m) for y in range(j,n)}):
                    return True
            
        return False
# @lc code=end