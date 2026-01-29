#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
from functools import lru_cache

class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7

        def count_upto(n_str):
            n_val = int(n_str)
            if n_val < 0: return 0
            if n_val == 0: return 1 # 0 is non-decreasing
            
            # Convert to base b digits
            digits = []
            temp = n_val
            while temp > 0:
                temp, rem = divmod(temp, b)
                digits.append(rem)
            digits = tuple(digits[::-1])
            num_digits = len(digits)

            @lru_cache(None)
            def dp(idx, prev, is_less, is_started):
                if idx == num_digits:
                    return 1
                
                res = 0
                limit = digits[idx] if not is_less else b - 1
                
                # If not started, we can place 0 and stay 'not started'
                if not is_started:
                    # Place 0
                    res = (res + dp(idx + 1, 0, is_less or (0 < limit), False)) % MOD
                    # Place 1 to limit
                    for d in range(1, limit + 1):
                        res = (res + dp(idx + 1, d, is_less or (d < limit), True)) % MOD
                else:
                    # Must be >= prev and <= limit
                    for d in range(prev, limit + 1):
                        res = (res + dp(idx + 1, d, is_less or (d < limit), True)) % MOD
                return res

            return dp(0, 0, False, False)

        # Standard range query: f(r) - f(l-1)
        # Note: l-1 is handled correctly by int(l)-1
        ans_r = count_upto(r)
        ans_l = count_upto(str(int(l) - 1))
        
        return (ans_r - ans_l + MOD) % MOD
# @lc code=end