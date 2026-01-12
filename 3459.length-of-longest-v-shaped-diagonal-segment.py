#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # Directions: Down-Right, Down-Left, Up-Left, Up-Right
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        # dp1[dir_idx][r][c]: Longest straight segment starting at (r, c)
        dp1 = [[[0] * m for _ in range(n)] for _ in range(4)]
        # dp0[dir_idx][r][c]: Longest segment starting at (r, c) with 1 turn available
        dp0 = [[[0] * m for _ in range(n)] for _ in range(4)]
        
        # Precompute dp1 (straight paths)
        for d in range(4):
            dr, dc = directions[d]
            rows = range(n)[::-1] if dr == 1 else range(n)
            cols = range(m)[::-1] if dc == 1 else range(m)
            for r in rows:
                for c in cols:
                    dp1[d][r][c] = 1
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2 - grid[r][c]:
                        dp1[d][r][c] = 1 + dp1[d][nr][nc]
        
        # Precompute dp0 (paths with at most one turn)
        for d in range(4):
            dr, dc = directions[d]
            nd = (d + 1) % 4
            ndr, ndc = directions[nd]
            rows = range(n)[::-1] if dr == 1 else range(n)
            cols = range(m)[::-1] if dc == 1 else range(m)
            for r in rows:
                for c in cols:
                    res = 1
                    target = 2 - grid[r][c]
                    # Option 1: Continue straight
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == target:
                        res = max(res, 1 + dp0[d][nr][nc])
                    # Option 2: Turn clockwise
                    tr, tc = r + ndr, c + ndc
                    if 0 <= tr < n and 0 <= tc < m and grid[tr][tc] == target:
                        res = max(res, 1 + dp1[nd][tr][tc])
                    dp0[d][r][c] = res
                    
        max_len = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    max_len = max(max_len, 1)
                    for d in range(4):
                        dr, dc = directions[d]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2:
                            max_len = max(max_len, 1 + dp0[d][nr][nc])
                            
        return max_len
# @lc code=end