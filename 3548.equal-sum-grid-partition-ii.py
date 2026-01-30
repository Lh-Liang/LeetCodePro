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
        # Precompute prefix sums for rows and columns
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        # Horizontal cuts
        upper = 0
        for i in range(m-1):
            upper += row_sums[i]
            lower = total - upper
            if upper == lower:
                return True
            diff = abs(upper - lower)
            # Try to discount one cell from either part
            # If upper > lower, need to discount from upper
            # Only edge row in each part can be discounted
            # For upper part (rows 0..i), can discount any cell in row i
            if upper > lower:
                for j in range(n):
                    if upper - grid[i][j] == lower:
                        # Removing grid[i][j] does not disconnect upper part (row i remains connected)
                        if n == 1 or m == 2: return True
                        if n > 1: return True # removing one cell from a row doesn't disconnect
            else:
                # Discount from lower part (row i+1)
                for j in range(n):
                    if lower - grid[i+1][j] == upper:
                        if n == 1 or m == 2: return True
                        if n > 1: return True
        # Vertical cuts
        left = 0
        for j in range(n-1):
            left += col_sums[j]
            right = total - left
            if left == right:
                return True
            diff = abs(left - right)
            # For vertical, can only discount from last column of left or first column of right section
            if left > right:
                for i in range(m):
                    if left - grid[i][j] == right:
                        if m == 1 or n == 2: return True
                        if m > 1: return True
            else:
                for i in range(m):
                    if right - grid[i][j+1] == left:
                        if m == 1 or n == 2: return True
                        if m > 1: return True
        return False
# @lc code=end