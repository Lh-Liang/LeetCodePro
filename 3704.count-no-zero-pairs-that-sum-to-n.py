#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
from functools import lru_cache

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        digits = list(map(int, str(n)))[::-1]  # least-significant first
        L = len(digits)

        @lru_cache(None)
        def dp(pos: int, carry: int, finA: int, finB: int) -> int:
            if pos == L:
                return 1 if carry == 0 else 0

            target = digits[pos]
            total = 0

            # Build allowed digits for a at this position
            if finA:
                a_choices = [(0, 1)]  # (digit, next_finA)
            else:
                a_choices = [(d, 0) for d in range(1, 10)]
                if pos > 0:
                    a_choices.append((0, 1))  # finish a here

            # Build allowed digits for b at this position
            if finB:
                b_choices = [(0, 1)]
            else:
                b_choices = [(d, 0) for d in range(1, 10)]
                if pos > 0:
                    b_choices.append((0, 1))

            for ad, nfinA in a_choices:
                for bd, nfinB in b_choices:
                    s = ad + bd + carry
                    if s % 10 == target:
                        total += dp(pos + 1, s // 10, nfinA, nfinB)

            return total

        # LSD cannot be 0 for positive no-zero integers, so both start as not finished.
        return dp(0, 0, 0, 0)
# @lc code=end
