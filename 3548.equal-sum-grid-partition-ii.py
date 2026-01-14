#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        def can_remove_and_stay_connected(num_rows, num_cols, r, c):
            if num_rows == 1:
                return c == 0 or c == num_cols - 1
            if num_cols == 1:
                return r == 0 or r == num_rows - 1
            return True
        
        # Try horizontal cuts
        for cut_row in range(m - 1):
            top_sum = sum(grid[i][j] for i in range(cut_row + 1) for j in range(n))
            bottom_sum = sum(grid[i][j] for i in range(cut_row + 1, m) for j in range(n))
            
            if top_sum == bottom_sum:
                return True
            
            diff = abs(top_sum - bottom_sum)
            num_top_rows = cut_row + 1
            num_bottom_rows = m - cut_row - 1
            
            if top_sum > bottom_sum:
                for i in range(num_top_rows):
                    for j in range(n):
                        if grid[i][j] == diff and can_remove_and_stay_connected(num_top_rows, n, i, j):
                            return True
            else:
                for i in range(cut_row + 1, m):
                    for j in range(n):
                        rel_i = i - cut_row - 1
                        if grid[i][j] == diff and can_remove_and_stay_connected(num_bottom_rows, n, rel_i, j):
                            return True
        
        # Try vertical cuts
        for cut_col in range(n - 1):
            left_sum = sum(grid[i][j] for i in range(m) for j in range(cut_col + 1))
            right_sum = sum(grid[i][j] for i in range(m) for j in range(cut_col + 1, n))
            
            if left_sum == right_sum:
                return True
            
            diff = abs(left_sum - right_sum)
            num_left_cols = cut_col + 1
            num_right_cols = n - cut_col - 1
            
            if left_sum > right_sum:
                for i in range(m):
                    for j in range(num_left_cols):
                        if grid[i][j] == diff and can_remove_and_stay_connected(m, num_left_cols, i, j):
                            return True
            else:
                for i in range(m):
                    for j in range(cut_col + 1, n):
                        rel_j = j - cut_col - 1
                        if grid[i][j] == diff and can_remove_and_stay_connected(m, num_right_cols, i, rel_j):
                            return True
        
        return False
# @lc code=end