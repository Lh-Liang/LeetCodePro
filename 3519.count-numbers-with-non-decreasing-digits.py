#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
import sys

# Increase recursion depth for deep DP trees
sys.setrecursionlimit(2000)

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        
        def get_base_b_digits(n, base):
            if n == 0: return [0]
            digits = []
            while n > 0:
                digits.append(n % base)
                n //= base
            return digits[::-1]

        def count_upto(num_str, base):
            if not num_str: return 0
            val = int(num_str)
            if val < 0: return 0
            digits = get_base_b_digits(val, base)
            n = len(digits)
            
            memo = {}

            def dp(idx, last_digit, is_less, is_started):
                state = (idx, last_digit, is_less, is_started)
                if state in memo: return memo[state]
                
                if idx == n:
                    return 1 if is_started else 0
                
                res = 0
                limit = digits[idx] if not is_less else base - 1
                
                for d in range(limit + 1):
                    new_is_less = is_less or (d < limit)
                    if not is_started:
                        if d == 0:
                            # Still leading zeros
                            res = (res + dp(idx + 1, 0, new_is_less, False)) % MOD
                        else:
                            # First non-zero digit
                            res = (res + dp(idx + 1, d, new_is_less, True)) % MOD
                    else:
                        # Already started, must be non-decreasing
                        if d >= last_digit:
                            res = (res + dp(idx + 1, d, new_is_less, True)) % MOD
                
                memo[state] = res
                return res

            # Add 1 to account for the number 0 which technically has non-decreasing digits
            # but DP logic usually starts from 1. However, the problem says "integers",
            # and 0 is non-decreasing. Let's adjust: dp returns count of non-decreasing > 0.
            return (dp(0, 0, False, False) + 1) % MOD

        ans_r = count_upto(r, b)
        ans_l_minus_1 = count_upto(str(int(l) - 1), b)
        
        return (ans_r - ans_l_minus_1 + MOD) % MOD
# @lc code=end