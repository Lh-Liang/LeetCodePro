#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
import sys
from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        # Directions: 0: BR, 1: BL, 2: TL, 3: TR
        # Clockwise turn: (i + 1) % 4
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        @lru_cache(None)
        def solve(r, c, d_idx, turned, expected):
            # Try continuing straight
            dr, dc = dirs[d_idx]
            nr, nc = r + dr, c + dc
            
            res = 0
            # Option 1: Continue straight
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == expected:
                res = 1 + solve(nr, nc, d_idx, turned, 2 if expected == 0 else 0)
            
            # Option 2: Turn clockwise (only if not turned yet)
            if not turned:
                nd_idx = (d_idx + 1) % 4
                dr2, dc2 = dirs[nd_idx]
                nr2, nc2 = r + dr2, c + dc2
                if 0 <= nr2 < n and 0 <= nc2 < m and grid[nr2][nc2] == expected:
                    res = max(res, 1 + solve(nr2, nc2, nd_idx, True, 2 if expected == 0 else 0))
            
            return res

        ans = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans = max(ans, 1)
                    for i in range(4):
                        dr, dc = dirs[i]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2:
                            ans = max(ans, 1 + 1 + solve(nr, nc, i, False, 0))
        
        return ans
# @lc code=end