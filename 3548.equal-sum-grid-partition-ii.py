#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        from collections import Counter

        def solve(g):
            R = len(g)
            C = len(g[0])
            if R < 2:
                return False
            
            total_sum = 0
            total_counts = Counter()
            row_sums = []
            
            # Precompute total sum and counts
            for r in range(R):
                s = 0
                for c in range(C):
                    val = g[r][c]
                    s += val
                    total_counts[val] += 1
                row_sums.append(s)
                total_sum += s
            
            top_sum = 0
            top_counts = Counter()
            
            # Iterate through horizontal cuts
            # A horizontal cut can be made after row i, where 0 <= i < R - 1
            for i in range(R - 1):
                # Update top section stats by adding row i
                top_sum += row_sums[i]
                for c in range(C):
                    top_counts[g[i][c]] += 1
                
                bot_sum = total_sum - top_sum
                diff = top_sum - bot_sum
                
                # Case 1: Sums are already equal
                if diff == 0:
                    return True
                
                # Case 2: Top sum is larger, try to remove from Top
                if diff > 0:
                    x = diff
                    # We need x to be available in Top
                    if top_counts[x] > 0:
                        # Check connectivity of Top after removing x
                        # Top section covers rows 0 to i
                        h_top = i + 1
                        
                        # If the section is "thin" (1D in either dimension), we must remove from ends
                        if h_top == 1 or C == 1:
                            valid = False
                            # If it's a single row (1 x C)
                            if h_top == 1:
                                if g[0][0] == x or g[0][C-1] == x: valid = True
                            # If it's a single column (h_top x 1)
                            elif C == 1:
                                if g[0][0] == x or g[i][0] == x: valid = True
                            
                            if valid:
                                return True
                        else:
                            # If dimensions are > 1 in both axes, removing any single cell keeps it connected
                            return True
                            
                # Case 3: Bottom sum is larger, try to remove from Bottom
                else:
                    y = -diff
                    # We need y to be available in Bottom
                    if total_counts[y] - top_counts[y] > 0:
                        # Check connectivity of Bottom
                        # Bottom section covers rows i+1 to R-1
                        h_bot = R - 1 - i
                        r_start = i + 1
                        r_end = R - 1
                        
                        if h_bot == 1 or C == 1:
                            valid = False
                            if h_bot == 1:
                                if g[r_start][0] == y or g[r_start][C-1] == y: valid = True
                            elif C == 1:
                                if g[r_start][0] == y or g[r_end][0] == y: valid = True
                            
                            if valid:
                                return True
                        else:
                            return True
            return False

        # Check horizontal cuts on original grid
        if solve(grid):
            return True
            
        # Check vertical cuts by transposing the grid
        # zip(*grid) returns tuples, convert to list of lists/tuples for indexing
        transposed_grid = list(zip(*grid))
        if solve(transposed_grid):
            return True
            
        return False
# @lc code=end