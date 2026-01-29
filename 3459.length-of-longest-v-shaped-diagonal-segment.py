#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
import sys

# Increase recursion depth for deep DP paths
sys.setrecursionlimit(2000000)

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # Directions: 0: (-1, -1), 1: (-1, 1), 2: (1, 1), 3: (1, -1)
        dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        
        memo = {}

        def get_len(r, c, d_idx, turned, target):
            state = (r, c, d_idx, turned, target)
            if state in memo:
                return memo[state]
            
            dr, dc = dirs[d_idx]
            nr, nc = r + dr, c + dc
            
            res = 0
            # Option 1: Continue in the same direction
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == target:
                res = 1 + get_len(nr, nc, d_idx, turned, 2 - target)
            
            # Option 2: Turn 90 degrees clockwise (only if not turned yet)
            if not turned:
                new_d_idx = (d_idx + 1) % 4
                ndr, ndc = dirs[new_d_idx]
                nnr, nnc = r + ndr, c + ndc
                if 0 <= nnr < n and 0 <= nnc < m and grid[nnr][nnc] == target:
                    res = max(res, 1 + get_len(nnr, nnc, new_d_idx, True, 2 - target))
            
            memo[state] = res
            return res

        max_len = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    max_len = max(max_len, 1) # A single '1' is a valid segment
                    for d_idx in range(4):
                        dr, dc = dirs[d_idx]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2:
                            # Start path: 1 (at r,c) -> 2 (at nr, nc)
                            max_len = max(max_len, 1 + 1 + get_len(nr, nc, d_idx, False, 0))
                            
        return max_len
# @lc code=end