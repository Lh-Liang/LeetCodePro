# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#
# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        
        def convert_to_base(num_str: str, base: int) -> list:
            return list(map(int, num_str))
        
        low = convert_to_base(l.zfill(len(r)), b)
        high = convert_to_base(r, b)
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(pos: int, prev_digit: int, tight_low: bool, tight_high: bool) -> int:
            if pos == len(high):
                return 1
            total_count = 0
            start = low[pos] if tight_low else 0
            end = high[pos] if tight_high else b - 1
            for digit in range(start, end + 1):
                if digit >= prev_digit:
                    total_count += dp(pos + 1, digit,
                                      tight_low and (digit == low[pos]),
                                      tight_high and (digit == high[pos]))
                    total_count %= MOD
            return total_count
        
        return dp(0, 0, True, True) % MOD
# @lc code=end