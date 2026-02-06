#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        max_length = 0
        
        # Directions for diagonals (dx, dy):
        directions = [((1,1), (-1,-1)), ((-1,-1), (1,1)), ((-1,1), (1,-1)), ((1,-1), (-1,1))]
        
        def valid_position(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < m 
        
        def trace_path(x: int, y: int, direction_pair) -> int:
            seq = [2, 0]
            seq_len = len(seq)
            length = 1 # Starting '1'
            idx = 0
            turns_used = False
            dir_idx = 0 # Start with first direction in pair
            while True:
                nx, ny = x + direction_pair[dir_idx][0], y + direction_pair[dir_idx][1]
                if valid_position(nx, ny) and grid[nx][ny] == seq[idx % seq_len]:
                    length += 1
                    idx += 1
                    x, y = nx, ny
                else:
                    # Check for one-time turn possibility if not yet used and not at end of current path
                    if not turns_used and dir_idx == 0:
                        nx_turned, ny_turned = x + direction_pair[1][0], y + direction_pair[1][1]
                        if valid_position(nx_turned, ny_turned) and grid[nx_turned][ny_turned] == seq[idx % seq_len]:
                            turns_used = True
                            dir_idx = 1 # Switch to second direction in pair after turn
                            length += 1
                            idx += 1
                            x, y = nx_turned, ny_turned
                        else:
                            break
                    else:
                        break
            return length if idx > 0 else -999 # Return -999 as invalid indicator if no progress was made beyond start.
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for dir_pair in directions:
                        max_length = max(max_length, trace_path(i, j, dir_pair))
        return max_length if max_length > -999 else 0 # Return zero if no valid sequence was found.
# @lc code=end