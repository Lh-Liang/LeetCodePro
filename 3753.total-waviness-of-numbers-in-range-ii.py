#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
import functools
from typing import Tuple

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def compute(num: int) -> int:
            if num < 0:
                return 0
            s = f"{num:016d}"
            @functools.lru_cache(None)
            def dp(pos: int, tight: int, start_idx: int, pp: int, p: int) -> tuple[int, int]:
                if pos == 16:
                    return 1, 0
                ans_c = 0
                ans_s = 0
                up = int(s[pos]) if tight == 1 else 9
                s_pos_digit = int(s[pos])
                for d in range(up + 1):
                    ntight = 1 if tight == 1 and d == s_pos_digit else 0
                    sp = start_idx - 1
                    nsp = sp if sp != -1 else (pos if d > 0 else -1)
                    nstart_idx = nsp + 1
                    npp = p
                    np = d
                    contrib = 0
                    if pos >= 2:
                        isp = sp
                        if isp != -1 and (pos - 1) >= isp + 1 and (pos - 1) <= 14:
                            middle = p
                            left = pp
                            right = d
                            if (middle > left and middle > right) or (middle < left and middle < right):
                                contrib = 1
                    sc, ss = dp(pos + 1, ntight, nstart_idx, npp, np)
                    ans_c += sc
                    ans_s += ss + contrib * sc
                return ans_c, ans_s
            return dp(0, 1, 0, 0, 0)[1]
        return compute(num2) - compute(num1 - 1)

# @lc code=end