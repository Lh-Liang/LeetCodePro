#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        
        def to_base_b(num_str):
            num = int(num_str)
            if num == 0:
                return [0]
            digits = []
            while num > 0:
                digits.append(num % b)
                num //= b
            return digits[::-1]
        
        def count_non_decreasing_up_to(num_str):
            digits = to_base_b(num_str)
            n = len(digits)
            
            from functools import lru_cache
            
            @lru_cache(maxsize=None)
            def dp(pos, last_digit, is_tight, has_started):
                if pos == n:
                    return 1 if has_started else 0
                
                max_digit = digits[pos] if is_tight else b - 1
                result = 0
                
                for digit in range(0, max_digit + 1):
                    new_is_tight = is_tight and (digit == digits[pos])
                    
                    if not has_started:
                        if digit == 0:
                            result = (result + dp(pos + 1, 0, new_is_tight, False)) % MOD
                        else:
                            result = (result + dp(pos + 1, digit, new_is_tight, True)) % MOD
                    else:
                        if digit >= last_digit:
                            result = (result + dp(pos + 1, digit, new_is_tight, True)) % MOD
                
                return result
            
            return dp(0, 0, True, False)
        
        count_r = count_non_decreasing_up_to(r)
        l_value = int(l)
        count_l_minus_1 = count_non_decreasing_up_to(str(l_value - 1)) if l_value > 0 else 0
        
        return (count_r - count_l_minus_1 + MOD) % MOD
# @lc code=end