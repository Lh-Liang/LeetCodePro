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
        total = 0
        row_sums = [0] * m
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                total += v
                row_sums[i] += v
                col_sums[j] += v
        prefix_row = [0] * (m + 1)
        for i in range(m):
            prefix_row[i + 1] = prefix_row[i] + row_sums[i]
        prefix_col = [0] * (n + 1)
        for j in range(n):
            prefix_col[j + 1] = prefix_col[j] + col_sums[j]
        # Dicts for prefixes 1 to m-1 and 1 to n-1
        row_dict = {prefix_row[h]: h for h in range(1, m)}
        col_dict = {prefix_col[w]: w for w in range(1, n)}
        # No discount horizontal
        for h in range(1, m):
            if prefix_row[h] * 2 == total:
                return True
        # No discount vertical
        for w in range(1, n):
            if prefix_col[w] * 2 == total:
                return True
        # Discounts horizontal
        for i in range(m):
            for j in range(n):
                V = grid[i][j]
                # Top discount horiz
                target = total + V
                if target % 2 == 0:
                    target_top = target // 2
                    if target_top in row_dict:
                        h_top = row_dict[target_top]
                        top_size = h_top * n
                        bot_size = (m - h_top) * n
                        if h_top >= i + 1 and top_size >= 2 and bot_size >= 1:
                            hh, ww = h_top, n
                            if min(hh, ww) >= 2:
                                return True
                            else:
                                # line
                                if hh == 1:  # horiz line row 0
                                    if i == 0 and (j == 0 or j == n - 1):
                                        return True
                                elif n == 1:  # vert line col 0
                                    if j == 0 and (i == 0 or i == h_top - 1):
                                        return True
                # Bottom discount horiz
                target2 = total - V
                if target2 % 2 == 0:
                    target_top2 = target2 // 2
                    if target_top2 in row_dict:
                        h_top = row_dict[target_top2]
                        top_size = h_top * n
                        bot_size = (m - h_top) * n
                        if h_top <= i and h_top >= 1 and top_size >= 1 and bot_size >= 2:
                            hh, ww = m - h_top, n
                            start_row = h_top
                            if min(hh, ww) >= 2:
                                return True
                            else:
                                if hh == 1:  # horiz line row start_row
                                    if i == start_row and (j == 0 or j == n - 1):
                                        return True
                                elif n == 1:  # vert line col 0, rows start_row to m-1
                                    if j == 0 and (i == start_row or i == m - 1):
                                        return True
        # Discounts vertical
        for i in range(m):
            for j in range(n):
                V = grid[i][j]
                # Left discount vert
                target = total + V
                if target % 2 == 0:
                    target_left = target // 2
                    if target_left in col_dict:
                        w_left = col_dict[target_left]
                        left_size = w_left * m
                        right_size = (n - w_left) * m
                        if w_left >= j + 1 and left_size >= 2 and right_size >= 1:
                            hh, ww = m, w_left
                            if min(hh, ww) >= 2:
                                return True
                            else:
                                if m == 1:  # horiz line row 0, cols 0 to w_left-1
                                    if i == 0 and (j == 0 or j == w_left - 1):
                                        return True
                                elif w_left == 1:  # vert line col 0
                                    if j == 0 and (i == 0 or i == m - 1):
                                        return True
                # Right discount vert
                target2 = total - V
                if target2 % 2 == 0:
                    target_left2 = target2 // 2
                    if target_left2 in col_dict:
                        w_left = col_dict[target_left2]
                        left_size = w_left * m
                        right_size = (n - w_left) * m
                        if w_left <= j and w_left >= 1 and left_size >= 1 and right_size >= 2:
                            hh, ww = m, n - w_left
                            start_col = w_left
                            if min(hh, ww) >= 2:
                                return True
                            else:
                                if m == 1:  # horiz line row 0, cols start_col to n-1
                                    if i == 0 and (j == start_col or j == n - 1):
                                        return True
                                elif n - w_left == 1:  # vert line col start_col
                                    if j == start_col and (i == 0 or i == m - 1):
                                        return True
        return False

# @lc code=end
