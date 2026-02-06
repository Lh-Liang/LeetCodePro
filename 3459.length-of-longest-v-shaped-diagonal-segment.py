#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        if n == 0 or m == 0: return 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # Directions – diagonals
        dp = [[[0]*4 for _ in range(m)] for _ in range(n)] # DP table for each direction
        max_length = 0
        # Fill dp table with initial values based on direct propagation of diagonals
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4): # For each direction
                        x, y = i + directions[d][0], j + directions[d][1]
                        if 0 <= x < n and 0 <= y < m and grid[x][y] == 2:
                            dp[i][j][d] = dp[x][y][d] + 2 # Alternating sequence continues as '2' then ‘0' etc.
                        max_length = max(max_length, dp[i][j][d]) # Update maximum length found so far
        return max_length # Return maximum length found in any direction
# @lc code=end