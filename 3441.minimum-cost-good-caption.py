#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        ords = [ord(ch) - ord('a') for ch in caption]
        INF = 10**9 * 100 + 7
        C = 26
        dp = [[[INF for _ in range(3)] for _ in range(C)] for _ in range(n + 1)]
        # init first
        for cc in range(C):
            dp[1][cc][0] = abs(ords[0] - cc)
        for i in range(1, n):
            for prev in range(C):
                for pk in range(3):
                    if dp[i][prev][pk] == INF:
                        continue
                    for nc in range(C):
                        add = abs(ords[i] - nc)
                        if nc == prev:
                            newk = min(pk + 1, 2)
                            dp[i + 1][nc][newk] = min(dp[i + 1][nc][newk], dp[i][prev][pk] + add)
                        elif pk == 2:
                            newk = 0
                            dp[i + 1][nc][newk] = min(dp[i + 1][nc][newk], dp[i][prev][pk] + add)
        min_cost = min(dp[n][c][2] for c in range(C))
        if min_cost == INF:
            return ""
        # back
        back = [[[INF for _ in range(3)] for _ in range(C)] for _ in range(n + 1)]
        for c in range(C):
            back[n][c][2] = 0
        for i in range(n - 1, -1, -1):
            for prev in range(C):
                for pk in range(3):
                    min_val = INF
                    for nc in range(C):
                        add = abs(ords[i] - nc)
                        allowed = False
                        newk = 0
                        if nc == prev:
                            allowed = True
                            newk = min(pk + 1, 2)
                        elif pk == 2:
                            allowed = True
                            newk = 0
                        if allowed:
                            min_val = min(min_val, add + back[i + 1][nc][newk])
                    back[i][prev][pk] = min_val
        # construct
        res = []
        cur_i = 0
        cur_cost = 0
        # first
        chosen = False
        for cc in range(C):
            add = abs(ords[0] - cc)
            tent_cost = add
            nk = 0
            if dp[1][cc][nk] == tent_cost and tent_cost + back[1][cc][nk] == min_cost:
                res.append(chr(ord('a') + cc))
                cur_c = cc
                cur_k = nk
                cur_cost = tent_cost
                cur_i = 1
                chosen = True
                break
        if not chosen:
            return ""
        while cur_i < n:
            chosen = False
            for cc in range(C):
                add = abs(ords[cur_i] - cc)
                tent_cost = cur_cost + add
                nc_ = cc
                if nc_ == cur_c:
                    nk = min(cur_k + 1, 2)
                elif cur_k == 2:
                    nk = 0
                else:
                    continue
                if dp[cur_i + 1][nc_][nk] == tent_cost and tent_cost + back[cur_i + 1][nc_][nk] == min_cost:
                    res.append(chr(ord('a') + cc))
                    cur_c = nc_
                    cur_k = nk
                    cur_cost = tent_cost
                    cur_i += 1
                    chosen = True
                    break
            if not chosen:
                return ""
        return ''.join(res)

# @lc code=end