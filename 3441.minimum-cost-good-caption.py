#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n == 0:
            return ""
        INF = float('inf')
        suf_dp = [[[INF] * 26 for _ in range(3)] for _ in range(n + 1)]
        for c in range(26):
            suf_dp[n][2][c] = 0
        for i in range(n - 1, -1, -1):
            for typ in range(3):
                for prev_c in range(26):
                    min_cost = INF
                    for d in range(26):
                        cost = abs(ord(caption[i]) - (ord('a') + d))
                        valid = False
                        nt = -1
                        nc = -1
                        if typ == 0:
                            if d == prev_c:
                                nt = 1
                                nc = prev_c
                                valid = True
                        elif typ == 1:
                            if d == prev_c:
                                nt = 2
                                nc = prev_c
                                valid = True
                        else:  # typ == 2
                            if d == prev_c:
                                nt = 2
                                nc = prev_c
                                valid = True
                            else:
                                nt = 0
                                nc = d
                                valid = True
                        if valid:
                            min_cost = min(min_cost, cost + suf_dp[i + 1][nt][nc])
                    suf_dp[i][typ][prev_c] = min_cost
        # Initial empty state at i=0
        suf_0 = INF
        for d in range(26):
            cost = abs(ord(caption[0]) - (ord('a') + d))
            suf_0 = min(suf_0, cost + suf_dp[1][0][d])
        if suf_0 == INF:
            return ""
        # Reconstruct lex smallest
        res = [''] * n
        current_i = 0
        # Start with empty
        found = False
        for d in range(26):
            cost_add = abs(ord(caption[0]) - (ord('a') + d))
            remaining = suf_dp[1][0][d]
            if remaining != INF and cost_add + remaining == suf_0:
                res[0] = chr(ord('a') + d)
                current_typ = 0
                current_c = d
                current_i = 1
                found = True
                break
        if not found:
            return ""
        # Continue
        while current_i < n:
            typ = current_typ
            prev_c = current_c
            found = False
            for d in range(26):
                cost_add = abs(ord(caption[current_i]) - (ord('a') + d))
                valid = False
                nt = -1
                nc = -1
                if typ == 0:
                    if d == prev_c:
                        nt = 1
                        nc = prev_c
                        valid = True
                elif typ == 1:
                    if d == prev_c:
                        nt = 2
                        nc = prev_c
                        valid = True
                else:  # typ == 2
                    if d == prev_c:
                        nt = 2
                        nc = prev_c
                        valid = True
                    else:
                        nt = 0
                        nc = d
                        valid = True
                if valid:
                    remaining = suf_dp[current_i + 1][nt][nc]
                    if remaining != INF and cost_add + remaining == suf_dp[current_i][typ][prev_c]:
                        res[current_i] = chr(ord('a') + d)
                        current_typ = nt
                        current_c = nc
                        current_i += 1
                        found = True
                        break
            if not found:
                return ""
        return ''.join(res)
# @lc code=end