#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # Directions: (row_delta, col_delta) for diagonals
        directions = [ (1, 1), (1, -1), (-1, 1), (-1, -1) ]
        n, m = len(grid), len(grid[0])

        # Precompute max alternating sequence (starting with 2 or 0) from each cell in all diagonals
        # dp[dir][i][j][phase]: for direction, position, and phase (0: expect 2, 1: expect 0)
        dp = [ [ [ [0,0] for _ in range(m) ] for _ in range(n) ] for _ in range(4) ]

        for d, (dr, dc) in enumerate(directions):
            # Traverse in direction so that dependencies are filled first
            r_range = range(n) if dr > 0 else range(n-1, -1, -1)
            c_range = range(m) if dc > 0 else range(m-1, -1, -1)
            for i in r_range:
                for j in c_range:
                    for phase in [0, 1]:
                        expect = 2 if phase == 0 else 0
                        ni, nj = i - dr, j - dc
                        if 0 <= ni < n and 0 <= nj < m:
                            if grid[i][j] == expect:
                                dp[d][i][j][phase] = 1 + dp[d][ni][nj][1 - phase]
                        else:
                            if grid[i][j] == expect:
                                dp[d][i][j][phase] = 1

        maxlen = 0
        # For every cell, try starting with 1, then for each direction, try to go as far as possible,
        # and at each position, optionally make a turn once to another diagonal (clockwise).
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                for d, (dr, dc) in enumerate(directions):
                    length = 1
                    x, y = i, j
                    phase = 0  # Next expect 2
                    steps = 0
                    # Move straight in this direction, counting as far as we can
                    while True:
                        x += dr
                        y += dc
                        steps += 1
                        if not (0 <= x < n and 0 <= y < m):
                            break
                        expect = 2 if phase == 0 else 0
                        if grid[x][y] != expect:
                            break
                        length += 1
                        phase ^= 1
                        # At each step, consider making a clockwise turn
                        nd = (d + 1) % 4
                        ndr, ndc = directions[nd]
                        nx, ny = x + ndr, y + ndc
                        if 0 <= nx < n and 0 <= ny < m:
                            # Next expect
                            nexp = 2 if phase == 0 else 0
                            if grid[nx][ny] == nexp:
                                # We can use precomputed dp for the rest after the turn
                                addlen = dp[nd][nx][ny][1 - phase]
                                maxlen = max(maxlen, length + addlen)
                    maxlen = max(maxlen, length)
        return maxlen
# @lc code=end