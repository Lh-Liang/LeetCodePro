#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        from functools import lru_cache
        digits = list(map(int, str(n)))[::-1]  # least significant first
        L = len(digits)
        
        @lru_cache(maxsize=None)
        def dp(pos, carry, tight):
            if pos == L:
                return 1 if carry == 0 else 0
            res = 0
            max_digit = digits[pos] if tight else 18  # since a_digit+b_digit can be up to 18
            for a in range(1, 10):
                for b in range(1, 10):
                    s = a + b + carry
                    if s % 10 == digits[pos] or (not tight):
                        new_carry = s // 10
                        # Check tightness
                        if tight and (a + b + carry) % 10 != digits[pos]:
                            continue
                        res += dp(pos + 1, new_carry, tight and (a + b + carry) % 10 == digits[pos])
            return res
        return dp(0, 0, True)
# @lc code=end