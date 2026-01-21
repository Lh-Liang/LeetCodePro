#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
from collections import Counter
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check_horizontal(g):
            rows = len(g)
            cols = len(g[0])
            if rows < 2:
                return False
            
            row_sums = [sum(row) for row in g]
            total_sum = sum(row_sums)
            total_freq = Counter()
            for row in g:
                for val in row:
                    total_freq[val] += 1
            
            sec1_freq = Counter()
            s1 = 0
            for i in range(rows - 1):
                for val in g[i]:
                    sec1_freq[val] += 1
                s1 += row_sums[i]
                s2 = total_sum - s1
                
                # Case 1: Equal sums
                if s1 == s2:
                    return True
                
                # Case 2: Discount x from Section 1
                x1 = 2 * s1 - total_sum
                if x1 > 0:
                    if (i + 1 > 1 and cols > 1):
                        if sec1_freq[x1] > 0:
                            return True
                    elif i + 1 == 1 and cols == 1:
                        if x1 == g[0][0]:
                            return True
                    elif i + 1 == 1:
                        if x1 == g[0][0] or x1 == g[0][cols - 1]:
                            return True
                    elif cols == 1:
                        if x1 == g[0][0] or x1 == g[i][0]:
                            return True
                
                # Case 3: Discount x from Section 2
                x2 = total_sum - 2 * s1
                if x2 > 0:
                    in_sec2 = (total_freq[x2] - sec1_freq[x2]) > 0
                    if in_sec2:
                        m2 = rows - i - 1
                        if (m2 > 1 and cols > 1):
                            return True
                        elif m2 == 1 and cols == 1:
                            if x2 == g[rows - 1][0]:
                                return True
                        elif m2 == 1:
                            if x2 == g[i + 1][0] or x2 == g[i + 1][cols - 1]:
                                return True
                        elif cols == 1:
                            if x2 == g[i + 1][0] or x2 == g[rows - 1][0]:
                                return True
            return False

        if check_horizontal(grid):
            return True
        
        # Transpose grid for vertical cuts
        transposed = list(zip(*grid))
        return check_horizontal(transposed)
# @lc code=end