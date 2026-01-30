#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        from functools import lru_cache
        s = str(n)[::-1]  # process from least significant digit
        L = len(s)

        @lru_cache(None)
        def dp(pos, carry, tight):
            if pos == L:
                return 1 if carry == 0 else 0
            res = 0
            max_digit = int(s[pos]) if tight else 9
            # For this position, try all combinations of digits 1-9 for a and b
            for da in range(1, 10):
                for db in range(1, 10):
                    sum_ab = da + db + carry
                    digit = sum_ab % 10
                    ncarry = sum_ab // 10
                    # The sum at this position must match n's digit if tight, otherwise any digit <= 9 is allowed
                    if tight:
                        if digit > max_digit:
                            continue
                        ntight = digit == max_digit
                    else:
                        ntight = False
                    res += dp(pos + 1, ncarry, ntight)
            return res
        # The DP ensures that no pair includes a zero digit, and only counts pairs whose sum matches n exactly
        return dp(0, 0, True)
# @lc code=end