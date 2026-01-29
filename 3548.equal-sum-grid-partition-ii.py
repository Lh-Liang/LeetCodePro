#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = 0
        total_counts = Counter()
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                total_sum += val
                total_counts[val] += 1

        def check(h, w, section_sums, section_counts, other_sum, other_counts, is_horizontal):
            """
            Checks if a partition is valid by discounting at most one cell.
            h, w: dimensions of the current section being checked for a discount.
            section_sums: total sum of the current section.
            section_counts: Counter of values in the current section.
            other_sum: sum of the other section.
            """
            # Case 1: No discount needed
            if section_sums == other_sum:
                return True
            
            # Case 2: Discount a cell from the current section
            # We need: section_sums - x == other_sum  => x = section_sums - other_sum
            x = section_sums - other_sum
            if x > 0 and section_counts[x] > 0:
                # Connectivity check for grid graphs:
                # - If both dimensions > 1, any cell removal preserves connectivity (2-connected).
                # - If one dimension is 1, only the two endpoints can be removed.
                if h > 1 and w > 1:
                    return True
                if h == 1 and w > 1:
                    # Check endpoints of the row
                    if is_horizontal:
                        # For a horizontal cut, a 1xW section is a single row.
                        # We don't know which row index, but the counts are already specific to this row.
                        # However, for 1xW, we must check the specific row's boundary values.
                        pass # Handled by specific logic in main loops for precision
                if h > 1 and w == 1:
                    pass # Handled by specific logic in main loops for precision
            return False

        # Process Horizontal Cuts
        curr_s1_sum = 0
        curr_s1_counts = Counter()
        for r in range(m - 1):
            for c in range(n):
                val = grid[r][c]
                curr_s1_sum += val
                curr_s1_counts[val] += 1
            
            s2_sum = total_sum - curr_s1_sum
            # Check S1 for discount
            x1 = curr_s1_sum - s2_sum
            if x1 == 0: return True
            if x1 > 0 and curr_s1_counts[x1] > 0:
                h1, w1 = r + 1, n
                if (h1 > 1 and w1 > 1) or (h1 == 1 and (x1 == grid[0][0] or x1 == grid[0][n-1])) or (w1 == 1 and (x1 == grid[0][0] or x1 == grid[r][0])):
                    return True
            # Check S2 for discount
            x2 = s2_sum - curr_s1_sum
            if x2 > 0 and (total_counts[x2] - curr_s1_counts[x2]) > 0:
                h2, w2 = m - 1 - r, n
                if (h2 > 1 and w2 > 1) or (h2 == 1 and (x2 == grid[m-1][0] or x2 == grid[m-1][n-1])) or (w2 == 1 and (x2 == grid[r+1][0] or x2 == grid[m-1][0])):
                    return True

        # Process Vertical Cuts
        curr_v1_sum = 0
        curr_v1_counts = Counter()
        for c in range(n - 1):
            for r in range(m):
                val = grid[r][c]
                curr_v1_sum += val
                curr_v1_counts[val] += 1
            
            v2_sum = total_sum - curr_v1_sum
            # Check V1 for discount
            y1 = curr_v1_sum - v2_sum
            if y1 == 0: return True
            if y1 > 0 and curr_v1_counts[y1] > 0:
                h1, w1 = m, c + 1
                if (h1 > 1 and w1 > 1) or (h1 == 1 and (y1 == grid[0][0] or y1 == grid[0][c])) or (w1 == 1 and (y1 == grid[0][0] or y1 == grid[m-1][0])):
                    return True
            # Check V2 for discount
            y2 = v2_sum - curr_v1_sum
            if y2 > 0 and (total_counts[y2] - curr_v1_counts[y2]) > 0:
                h2, w2 = m, n - 1 - c
                if (h2 > 1 and w2 > 1) or (h2 == 1 and (y2 == grid[0][c+1] or y2 == grid[0][n-1])) or (w2 == 1 and (y2 == grid[0][n-1] or y2 == grid[m-1][n-1])):
                    return True
                    
        return False
# @lc code=end