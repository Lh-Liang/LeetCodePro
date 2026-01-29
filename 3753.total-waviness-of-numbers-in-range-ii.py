#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(num: int) -> int:
            if num <= 0:
                return 0
            S = [int(c) for c in str(num)]
            L = len(S)
            memo = {}
            def dfs(pos: int, tight: int, prev: int, pprev: int) -> tuple[int, int]:
                if pos == L:
                    return 0, 1 if prev != 10 else 0
                key = (pos, tight, prev, pprev)
                if key in memo:
                    return memo[key]
                res_sum = 0
                res_cnt = 0
                up = S[pos] if tight == 1 else 9
                for d in range(up + 1):
                    nt = 1 if tight == 1 and d == S[pos] else 0
                    if prev == 10 and d == 0:
                        ssum, scnt = dfs(pos + 1, nt, 10, 10)
                        res_sum += ssum
                        res_cnt += scnt
                    else:
                        curr = d
                        if prev == 10:
                            np = curr
                            npp = 10
                        else:
                            np = curr
                            npp = prev
                        ssum, scnt = dfs(pos + 1, nt, np, npp)
                        contrib = 0
                        if prev != 10 and pprev != 10:
                            p_digit = prev
                            pp_digit = pprev
                            c_digit = curr
                            if (p_digit > pp_digit and p_digit > c_digit) or (p_digit < pp_digit and p_digit < c_digit):
                                contrib = scnt
                        res_sum += ssum + contrib
                        res_cnt += scnt
                memo[key] = (res_sum, res_cnt)
                return memo[key]
            return dfs(0, 1, 10, 10)[0]
        return calc(num2) - calc(num1 - 1)
# @lc code=end