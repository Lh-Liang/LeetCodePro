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

        def to_digits(x):
            if x == '0': return [0]
            res = []
            n = int(x)
            while n > 0:
                res.append(n % b)
                n //= b
            return res[::-1] if res else [0]

        def minus_one(s):
            # s is a string representing a decimal number, subtract 1 and return string
            s = list(s)
            i = len(s) - 1
            while i >= 0:
                if s[i] != '0':
                    s[i] = str(int(s[i])-1)
                    break
                s[i] = '9'
                i -= 1
            res = ''.join(s).lstrip('0')
            return res if res else '0'

        def count(bound):
            digits = to_digits(bound)
            n = len(digits)
            @lru_cache(maxsize=None)
            def dp(pos, prev, tight, leading_zero):
                if pos == n:
                    return 0 if leading_zero else 1
                ans = 0
                up = digits[pos] if tight else b - 1
                for d in range(0, up+1):
                    if not leading_zero:
                        if d < prev:
                            continue
                    next_leading_zero = leading_zero and (d == 0)
                    next_prev = d if not next_leading_zero else 0
                    ans = (ans + dp(pos+1, next_prev, tight and d==up, next_leading_zero)) % MOD
                return ans
            return dp(0, 0, True, True)

        l_minus_1 = minus_one(l)
        ans = (count(r) - count(l_minus_1)) % MOD
        return ans
# @lc code=end