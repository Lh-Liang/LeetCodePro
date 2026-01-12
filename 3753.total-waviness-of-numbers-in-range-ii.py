#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
import sys
from functools import lru_cache

sys.setrecursionlimit(2000)

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_total_waviness(n: int) -> int:
            if n < 100:
                return 0
            s = str(n)
            L = len(s)

            @lru_cache(None)
            def solve(pos, p1, p2, is_less, s_len):
                if pos == L:
                    return 1, 0
                
                res_cnt, res_wav = 0, 0
                limit = int(s[pos]) if not is_less else 9
                
                for d in range(limit + 1):
                    n_is_less = is_less or (d < limit)
                    
                    if s_len == 0:
                        if d == 0:
                            cnt, wav = solve(pos + 1, 0, 0, n_is_less, 0)
                        else:
                            cnt, wav = solve(pos + 1, d, 0, n_is_less, 1)
                        res_cnt += cnt
                        res_wav += wav
                    else:
                        inc = 0
                        if s_len >= 2:
                            # Check if p1 is a peak or valley relative to p2 and d
                            if (p2 < p1 > d) or (p2 > p1 < d):
                                inc = 1
                        cnt, wav = solve(pos + 1, d, p1, n_is_less, s_len + 1)
                        res_cnt += cnt
                        res_wav += (cnt * inc + wav)
                
                return res_cnt, res_wav

            return solve(0, 0, 0, False, 0)[1]

        return get_total_waviness(num2) - get_total_waviness(num1 - 1)
# @lc code=end