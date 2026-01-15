#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        from bisect import bisect_left
        
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        value_to_rows = {}
        value_to_cols = {}
        
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if v not in value_to_rows:
                    value_to_rows[v] = set()
                    value_to_cols[v] = set()
                value_to_rows[v].add(i)
                value_to_cols[v].add(j)
        
        for v in value_to_rows:
            value_to_rows[v] = sorted(value_to_rows[v])
            value_to_cols[v] = sorted(value_to_cols[v])
        
        def value_in_row_range(v, r_start, r_end):
            if v not in value_to_rows:
                return False
            rows = value_to_rows[v]
            idx = bisect_left(rows, r_start)
            return idx < len(rows) and rows[idx] <= r_end
        
        def value_in_col_range(v, c_start, c_end):
            if v not in value_to_cols:
                return False
            cols = value_to_cols[v]
            idx = bisect_left(cols, c_start)
            return idx < len(cols) and cols[idx] <= c_end
        
        def can_remove_from_top(target_val, r):
            section_size = (r + 1) * n
            if section_size == 1:
                return False
            if r == 0:
                return grid[0][0] == target_val or grid[0][n-1] == target_val
            if n == 1:
                return grid[0][0] == target_val or grid[r][0] == target_val
            return value_in_row_range(target_val, 0, r)
        
        def can_remove_from_bottom(target_val, r):
            section_size = (m - r - 1) * n
            if section_size == 1:
                return False
            if r == m - 2:
                return grid[m-1][0] == target_val or grid[m-1][n-1] == target_val
            if n == 1:
                return grid[r+1][0] == target_val or grid[m-1][0] == target_val
            return value_in_row_range(target_val, r + 1, m - 1)
        
        def can_remove_from_left(target_val, c):
            section_size = m * (c + 1)
            if section_size == 1:
                return False
            if c == 0:
                return grid[0][0] == target_val or grid[m-1][0] == target_val
            if m == 1:
                return grid[0][0] == target_val or grid[0][c] == target_val
            return value_in_col_range(target_val, 0, c)
        
        def can_remove_from_right(target_val, c):
            section_size = m * (n - c - 1)
            if section_size == 1:
                return False
            if c == n - 2:
                return grid[0][n-1] == target_val or grid[m-1][n-1] == target_val
            if m == 1:
                return grid[0][c+1] == target_val or grid[0][n-1] == target_val
            return value_in_col_range(target_val, c + 1, n - 1)
        
        top_sum = 0
        for r in range(m - 1):
            top_sum += row_sums[r]
            bottom_sum = total - top_sum
            
            if top_sum == bottom_sum:
                return True
            
            diff = top_sum - bottom_sum
            if diff > 0 and can_remove_from_top(diff, r):
                return True
            if diff < 0 and can_remove_from_bottom(-diff, r):
                return True
        
        left_sum = 0
        for c in range(n - 1):
            left_sum += col_sums[c]
            right_sum = total - left_sum
            
            if left_sum == right_sum:
                return True
            
            diff = left_sum - right_sum
            if diff > 0 and can_remove_from_left(diff, c):
                return True
            if diff < 0 and can_remove_from_right(-diff, c):
                return True
        
        return False
# @lc code=end