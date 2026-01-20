#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n, m_ = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        clock90 = [1, 3, 0, 2]
        prefix = [[[0] * 4 for _ in range(m_)] for _ in range(n)]
        forward_even = [[[0] * 4 for _ in range(m_)] for _ in range(n)]
        forward_odd = [[[0] * 4 for _ in range(m_)] for _ in range(n)]

        def req(t: int) -> int:
            return 1 if t == 0 else 2 if t % 2 == 1 else 0

        ans = 0
        for d in range(4):
            dr, dc = dirs[d]
            for i in range(n):
                for j in range(m_):
                    pi = i - dr
                    pj = j - dc
                    if 0 <= pi < n and 0 <= pj < m_:
                        continue
                    # build line
                    line = []
                    ci, cj = i, j
                    while 0 <= ci < n and 0 <= cj < m_:
                        line.append((ci, cj))
                        ci += dr
                        cj += dc
                    sz = len(line)
                    if sz == 0:
                        continue
                    # compute forwards backward
                    for k in range(sz - 1, -1, -1):
                        rr, cc = line[k]
                        # even: 0,2,0,2...
                        fwd_e = 0
                        if grid[rr][cc] == 0:
                            if k + 1 == sz:
                                fwd_e = 1
                            else:
                                nr2, nc2 = line[k + 1]
                                fwd_e = 1 + forward_odd[nr2][nc2][d]
                        forward_even[rr][cc][d] = fwd_e
                        # odd: 2,0,2,0...
                        fwd_o = 0
                        if grid[rr][cc] == 2:
                            if k + 1 == sz:
                                fwd_o = 1
                            else:
                                nr2, nc2 = line[k + 1]
                                fwd_o = 1 + forward_even[nr2][nc2][d]
                        forward_odd[rr][cc][d] = fwd_o
                    # straights and prefix
                    for s in range(sz):
                        sr, sc = line[s]
                        if grid[sr][sc] != 1:
                            continue
                        curlen = 1
                        ans = max(ans, curlen)
                        cs = s
                        tpos = 1
                        while cs + 1 < sz and grid[line[cs + 1][0]][line[cs + 1][1]] == req(tpos):
                            cs += 1
                            curlen += 1
                            tpos += 1
                            ans = max(ans, curlen)
                        er, ec = line[cs]
                        prefix[er][ec][d] = max(prefix[er][ec][d], curlen)
        # turns
        for d in range(4):
            dp_ = clock90[d]
            drp, dcp = dirs[dp_]
            for r in range(n):
                for c in range(m_):
                    l = prefix[r][c][d]
                    if l < 2:
                        continue
                    ur = r + drp
                    uc = c + dcp
                    if not (0 <= ur < n and 0 <= uc < m_):
                        continue
                    extra = forward_even[ur][uc][dp_] if l % 2 == 0 else forward_odd[ur][uc][dp_]
                    total = l + extra
                    ans = max(ans, total)
        return ans

# @lc code=end
