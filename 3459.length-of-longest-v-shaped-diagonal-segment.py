#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        from typing import List
        n, m = len(grid), len(grid[0])
        # Directions: (dr, dc) for 4 diagonals (NE, SE, SW, NW)
        diags = [(-1,1), (1,1), (1,-1), (-1,-1)]
        # dp[i][j][d][p]: max length from (i,j) in direction d, expecting value p (p=0 for 2, p=1 for 0), no turn
        dp = [[[[0, 0] for _ in range(4)] for _ in range(m)] for _ in range(n)]
        # Precompute DP for all four diagonal directions and both alternation states
        for d, (dr, dc) in enumerate(diags):
            rows = range(n) if dr > 0 else range(n-1, -1, -1)
            cols = range(m) if dc > 0 else range(m-1, -1, -1)
            for i in rows:
                for j in cols:
                    # Start of segment must be 1
                    if grid[i][j] == 1:
                        dp[i][j][d][0] = 1
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 2:
                            dp[i][j][d][0] = 1 + (dp[ni][nj][d][1])
                    # For alternation state expecting 0 (i.e., next should be 0)
                    if grid[i][j] == 0:
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 2:
                            dp[i][j][d][1] = 1 + (dp[ni][nj][d][0])
        maxlen = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                for d in range(4):
                    # No turn: maximum from this start in this direction
                    maxlen = max(maxlen, dp[i][j][d][0])
                    # Try all possible single-turn points
                    dr1, dc1 = diags[d]
                    ci, cj = i, j
                    altern = 0 # 0 means expecting 2, 1 means expecting 0
                    for step in range(1, dp[i][j][d][0]):
                        ci += dr1
                        cj += dc1
                        altern ^= 1
                        # After step steps, try a clockwise turn
                        nd = (d + 1) % 4
                        if 0 <= ci < n and 0 <= cj < m:
                            # The next segment after the turn must continue the alternation
                            cont = dp[ci][cj][nd][altern]
                            if cont > 0:
                                maxlen = max(maxlen, step + cont)
        return maxlen
# @lc code=end