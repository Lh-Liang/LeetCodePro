#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # Directions: 0: UL (-1,-1), 1: UR (-1,1), 2: DR (1,1), 3: DL (1,-1)
        dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        
        # dp[r][c][dir][has_turned] 
        # We use memoization to compute the longest sequence starting at (r, c)
        # as a specific part of the V-shape.
        import sys
        sys.setrecursionlimit(2000000)
        
        memo = {}

        def solve(r, c, d, has_turned, expected_val):
            state = (r, c, d, has_turned, expected_val)
            if state in memo: return memo[state]
            
            res = 1
            # Next cell in the current direction
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            next_val = 2 if expected_val == 0 else 0
            
            # Option 1: Continue straight
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == next_val:
                res = max(res, 1 + solve(nr, nc, d, has_turned, next_val))
            
            # Option 2: Turn 90 degrees clockwise (only if not already turned)
            if not has_turned:
                nd = (d + 1) % 4
                tr, tc = r + dirs[nd][0], c + dirs[nd][1]
                if 0 <= tr < n and 0 <= tc < m and grid[tr][tc] == next_val:
                    res = max(res, 1 + solve(tr, tc, nd, True, next_val))
            
            memo[state] = res
            return res

        max_len = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    max_len = max(max_len, 1)
                    for d in range(4):
                        nr, nc = r + dirs[d][0], c + dirs[d][1]
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2:
                            max_len = max(max_len, 1 + solve(nr, nc, d, False, 2))
                            
        return max_len
# @lc code=end