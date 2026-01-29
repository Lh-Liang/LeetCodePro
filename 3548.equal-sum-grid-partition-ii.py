#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def solve(mat):
            m = len(mat)
            n = len(mat[0])
            if m < 2:
                return False
            
            row_sums = [sum(row) for row in mat]
            total_sum = sum(row_sums)
            
            # b_counter tracks counts of values in the current bottom section (rows [i+1, m-1])
            b_counter = Counter()
            for r in range(1, m):
                for val in mat[r]:
                    b_counter[val] += 1
            
            # a_elements_seen tracks existence of values in the current top section (rows [0, i])
            # For 2D sections, existence is enough for connectivity.
            a_elements_seen = Counter()
            s_a = 0
            
            for i in range(m - 1):
                s_a += row_sums[i]
                s_b = total_sum - s_a
                
                for val in mat[i]:
                    a_elements_seen[val] += 1
                
                # Case 1: No discounting needed
                if s_a == s_b:
                    return True
                
                # Case 2: Discount x from Section A
                if s_a > s_b:
                    x = s_a - s_b
                    # Connectivity check for A (rows 0 to i)
                    if n == 1: # A is a column
                        if x == mat[0][0] or x == mat[i][0]:
                            return True
                    elif i == 0: # A is a single row
                        if x == mat[0][0] or x == mat[0][n-1]:
                            return True
                    else: # A is 2D, any cell removal preserves connectivity
                        if a_elements_seen[x] > 0:
                            return True
                
                # Case 3: Discount y from Section B
                if s_b > s_a:
                    y = s_b - s_a
                    # Connectivity check for B (rows i+1 to m-1)
                    if n == 1: # B is a column
                        if y == mat[i+1][0] or y == mat[m-1][0]:
                            return True
                    elif i == m - 2: # B is a single row
                        if y == mat[m-1][0] or y == mat[m-1][n-1]:
                            return True
                    else: # B is 2D
                        if b_counter[y] > 0:
                            return True
                
                # Update b_counter for the next cut position
                if i < m - 2:
                    for val in mat[i+1]:
                        b_counter[val] -= 1
                        if b_counter[val] == 0:
                            del b_counter[val]
            
            return False

        # Check horizontal cuts
        if solve(grid):
            return True
        
        # Check vertical cuts by transposing the grid
        transposed = list(zip(*grid))
        return solve(transposed)
# @lc code=end