#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
from functools import lru_cache
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # DR, DL, UL, UR
        
        @lru_cache(maxsize=None)
        def straight(r, c, d, parity):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 0
            expected = 2 if parity == 0 else 0
            if grid[r][c] != expected:
                return 0
            dr, dc = directions[d]
            return 1 + straight(r + dr, c + dc, d, 1 - parity)
        
        ans = 0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    for d in range(4):
                        dr, dc = directions[d]
                        d_turn = (d + 1) % 4
                        dr_turn, dc_turn = directions[d_turn]
                        
                        # No turn: straight path
                        length = 1 + straight(r + dr, c + dc, d, 0)
                        ans = max(ans, length)
                        
                        # Turn at position 1, 2, 3, ...
                        cr, cc = r, c
                        pos = 0
                        while True:
                            nr, nc = cr + dr, cc + dc
                            pos += 1
                            
                            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                                break
                            expected = 2 if pos % 2 == 1 else 0
                            if grid[nr][nc] != expected:
                                break
                            
                            cr, cc = nr, nc
                            
                            # Turn at position pos
                            next_r, next_c = cr + dr_turn, cc + dc_turn
                            next_parity = pos % 2
                            
                            suffix = straight(next_r, next_c, d_turn, next_parity)
                            length = (pos + 1) + suffix
                            ans = max(ans, length)
        
        return ans
# @lc code=end