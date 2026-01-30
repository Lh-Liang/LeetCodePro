#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        from functools import lru_cache

        def count_waviness(n):
            digits = list(map(int, str(n)))
            L = len(digits)

            @lru_cache(maxsize=None)
            def dp(pos, tight, lead, prev2, prev1):
                if pos == L:
                    return 0
                res = 0
                hi = digits[pos] if tight else 9
                for d in range(0, hi + 1):
                    nlead = lead and (d == 0)
                    ntight = tight and (d == hi)
                    if lead and d == 0:
                        res += dp(pos + 1, ntight, True, -1, -1)
                    else:
                        wave = 0
                        if not lead and pos >= 2:
                            # Check if prev1 is peak or valley
                            if prev1 > prev2 and prev1 > d:
                                wave = 1
                            elif prev1 < prev2 and prev1 < d:
                                wave = 1
                        res += wave + dp(pos + 1, ntight, False, prev1, d)
                return res

            return dp(0, True, True, -1, -1)

        def get_ans(a, b):
            return count_waviness(b) - count_waviness(a - 1)

        return get_ans(num1, num2)
# @lc code=end