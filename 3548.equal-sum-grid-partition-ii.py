#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        if not grid or not grid[0]:
            return False
        m, n = len(grid), len(grid[0])
        T = 0
        row_sum = [0] * m
        col_sum = [0] * n
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                T += v
                row_sum[i] += v
                col_sum[j] += v
        # prefix_row[r] = sum of first r rows (0 to r-1)
        prefix_row = [0] * (m + 1)
        for i in range(m):
            prefix_row[i + 1] = prefix_row[i] + row_sum[i]
        sum_to_r = {}
        for r in range(1, m):
            s = prefix_row[r]
            if 2 * s == T:
                return True
            sum_to_r[s] = r
        # prefix_col[c] = sum of first c cols
        prefix_col = [0] * (n + 1)
        for j in range(n):
            prefix_col[j + 1] = prefix_col[j] + col_sum[j]
        sum_to_c = {}
        for c in range(1, n):
            s = prefix_col[c]
            if 2 * s == T:
                return True
            sum_to_c[s] = c
        def can_remove(H: int, W: int, rr: int, rc: int) -> bool:
            if H >= 2 and W >= 2:
                return True
            if H == 1 and W == 1:
                return False
            if H == 1:  # W >= 2, horizontal line
                return rc == 0 or rc == W - 1
            if W == 1:  # H >= 2, vertical line
                return rr == 0 or rr == H - 1
            return False
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                # Horizontal: discount upper (remove from upper section)
                if (T + v) % 2 == 0:
                    target = (T + v) // 2
                    if target in sum_to_r:
                        r = sum_to_r[target]
                        if i < r and can_remove(r, n, i, j):
                            return True
                # Horizontal: discount lower
                if (T - v) % 2 == 0:
                    target = (T - v) // 2
                    if target >= 0 and target in sum_to_r:
                        r = sum_to_r[target]
                        if i >= r and can_remove(m - r, n, i - r, j):
                            return True
                # Vertical: discount left
                if (T + v) % 2 == 0:
                    target = (T + v) // 2
                    if target in sum_to_c:
                        c = sum_to_c[target]
                        if j < c and can_remove(m, c, i, j):
                            return True
                # Vertical: discount right
                if (T - v) % 2 == 0:
                    target = (T - v) // 2
                    if target >= 0 and target in sum_to_c:
                        c = sum_to_c[target]
                        if j >= c and can_remove(m, n - c, i, j - c):
                            return True
        return False

# @lc code=end