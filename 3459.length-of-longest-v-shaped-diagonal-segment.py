#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
import sys

# Increase recursion depth for deep diagonal paths
sys.setrecursionlimit(2000000)

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # Directions: 0: (1,1), 1: (1,-1), 2: (-1,-1), 3: (-1,1)
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        # Use a 4D memoization array for performance: [row][col][direction][has_turned]
        # We don't need expected_val in state because the path is deterministic
        memo = [[[[-1] * 2 for _ in range(4)] for _ in range(C)] for _ in range(R)]

        def get_max_len(r, c, dir_idx, turned, current_val):
            if memo[r][c][dir_idx][turned] != -1:
                return memo[r][c][dir_idx][turned]
            
            res = 1
            next_val = 2 if current_val == 0 else 0
            
            # Option 1: Continue straight
            dr, dc = dirs[dir_idx]
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == next_val:
                res = max(res, 1 + get_max_len(nr, nc, dir_idx, turned, next_val))
            
            # Option 2: Turn clockwise (only if not turned yet)
            if not turned:
                new_dir_idx = (dir_idx + 1) % 4
                ndr, ndc = dirs[new_dir_idx]
                nnr, nnc = r + ndr, c + ndc
                if 0 <= nnr < R and 0 <= nnc < C and grid[nnr][nnc] == next_val:
                    res = max(res, 1 + get_max_len(nnr, nnc, new_dir_idx, 1, next_val))
            
            memo[r][c][dir_idx][turned] = res
            return res

        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    ans = max(ans, 1)
                    for i in range(4):
                        dr, dc = dirs[i]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 2:
                            # Start: 1 -> 2. Next expected in DFS is 0.
                            ans = max(ans, 1 + get_max_len(nr, nc, i, 0, 2))
        
        return ans
# @lc code=end