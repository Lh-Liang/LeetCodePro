#
# @lc app=leetcode id=3459 lang=python3
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        dp = [[[[0] * 2 for _ in range(m)] for _ in range(n)] for _ in range(4)]
        
        # Precompute dp[d][r][c][t]: max ext steps AFTER (r,c), t=0 expect0 first/next, t=1 expect2 first/next
        for d_idx in range(4):
            dr, dc = dirs[d_idx]
            for r in range(n):
                for c in range(m):
                    pr, pc = r - dr, c - dc
                    if 0 <= pr < n and 0 <= pc < m:
                        continue
                    # chain head: build forward chain
                    chain = []
                    cr, cc = r, c
                    while 0 <= cr < n and 0 <= cc < m:
                        chain.append((cr, cc))
                        cr += dr
                        cc += dc
                    clen = len(chain)
                    if clen == 0:
                        continue
                    # end of chain
                    er, ec = chain[-1]
                    dp[d_idx][er][ec][0] = 0
                    dp[d_idx][er][ec][1] = 0
                    for ji in range(clen - 2, -1, -1):
                        cr, cc = chain[ji]
                        nr, nc = chain[ji + 1]
                        for typ in range(2):
                            vreq = 2 * typ
                            if grid[nr][nc] == vreq:
                                subtyp = 1 - typ
                                dp[d_idx][cr][cc][typ] = 1 + dp[d_idx][nr][nc][subtyp]
                            else:
                                dp[d_idx][cr][cc][typ] = 0
        
        ans = 0
        # Straight and single
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans = max(ans, 1)
                    for d_idx in range(4):
                        ext = dp[d_idx][r][c][1]
                        ans = max(ans, 1 + ext)
        
        # V-shapes: pre-turn d0, post-turn d1=(d0+1)%4
        for d0 in range(4):
            d1 = (d0 + 1) % 4
            dr, dc = dirs[d0]
            for r in range(n):
                for c in range(m):
                    pr, pc = r - dr, c - dc
                    if 0 <= pr < n and 0 <= pc < m:
                        continue
                    chain = []
                    cr, cc = r, c
                    while 0 <= cr < n and 0 <= cc < m:
                        chain.append((cr, cc))
                        cr += dr
                        cc += dc
                    clen = len(chain)
                    if clen < 2:
                        continue
                    dq = deque()
                    for j in range(clen):
                        # Clean front: remove starts that cannot reach j
                        while dq and (dq[0] + dp[d0][chain[dq[0]][0]][chain[dq[0]][1]][1] < j):
                            dq.popleft()
                        # Compute V if possible (max prefix from leftmost reaching start)
                        if dq:
                            min_js = dq[0]
                            prefix_len = j - min_js + 1
                            if prefix_len >= 2:
                                tr, tc = chain[j]
                                t = prefix_len - 1
                                suffix_typ = 1 if (t % 2 == 0) else 0
                                ext_suf = dp[d1][tr][tc][suffix_typ]
                                total = prefix_len + ext_suf
                                ans = max(ans, total)
                        # Add current if it's a start (1)
                        trr, tcc = chain[j]
                        if grid[trr][tcc] == 1:
                            dq.append(j)
        return ans
# @lc code=end