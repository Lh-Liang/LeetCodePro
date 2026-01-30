#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        from functools import lru_cache
        
        def to_base_digits(x: str, base: int) -> list:
            digits = []
            num = int(x)
            if num == 0:
                return [0]
            while num > 0:
                digits.append(num % base)
                num //= base
            return digits[::-1]

        def count_non_decreasing(digits):
            n = len(digits)
            @lru_cache(maxsize=None)
            def dp(pos, last_digit, tight, started):
                if pos == n:
                    return int(started)
                res = 0
                max_digit = digits[pos] if tight else b-1
                for d in range(0, max_digit+1):
                    if not started and d == 0:
                        res += dp(pos+1, 0, tight and d == max_digit, False)
                    elif not started or d >= last_digit:
                        res += dp(pos+1, d, tight and d == max_digit, True)
                return res % MOD
            return dp(0, 0, True, False)

        def decrement_str(x: str) -> str:
            # Helper to compute x-1 as a string
            num = int(x)
            if num == 0: return '0'
            return str(num-1)

        r_digits = to_base_digits(r, b)
        l_minus_1_digits = to_base_digits(decrement_str(l), b)
        count_r = count_non_decreasing(r_digits)
        count_l_minus_1 = count_non_decreasing(l_minus_1_digits)
        return (count_r - count_l_minus_1) % MOD
# @lc code=end