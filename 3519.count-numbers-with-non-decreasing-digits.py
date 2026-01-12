#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
import functools

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7

        def to_base_b(n_str, base):
            n = int(n_str)
            if n == 0: return [0]
            digits = []
            while n > 0:
                digits.append(n % base)
                n //= base
            return digits[::-1]

        @functools.lru_cache(None)
        def solve_dp(idx, last_digit, is_less, is_started, digits_tuple, base):
            if idx == len(digits_tuple):
                return 1 if is_started else 0
            
            res = 0
            upper = digits_tuple[idx] if not is_less else base - 1
            
            for d in range(upper + 1):
                if not is_started:
                    if d == 0:
                        res = (res + solve_dp(idx + 1, 0, True, False, digits_tuple, base)) % MOD
                    else:
                        res = (res + solve_dp(idx + 1, d, is_less or (d < upper), True, digits_tuple, base)) % MOD
                else:
                    if d >= last_digit:
                        res = (res + solve_dp(idx + 1, d, is_less or (d < upper), True, digits_tuple, base)) % MOD
            return res

        def count_upto(s, base):
            digits = to_base_b(s, base)
            solve_dp.cache_clear()
            return solve_dp(0, 0, False, False, tuple(digits), base)

        ans_r = count_upto(r, b)
        l_minus_1 = str(int(l) - 1)
        ans_l = count_upto(l_minus_1, b) if int(l) > 0 else 0
        
        return (ans_r - ans_l + MOD) % MOD
# @lc code=end