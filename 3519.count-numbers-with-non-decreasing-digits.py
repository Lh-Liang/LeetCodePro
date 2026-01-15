#
# @lc app=leetcode id=3519 lang=python3
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7
        
        def to_base(s, base):
            if s == "0":
                return [0]
            digits = []
            while s != "0":
                remainder = 0
                new_s = ""
                for c in s:
                    val = remainder * 10 + int(c)
                    new_s += str(val // base)
                    remainder = val % base
                digits.append(remainder)
                s = new_s.lstrip("0") or "0"
            return digits[::-1]
        
        def subtract_one(s):
            if s == "0":
                return "-1"
            digits = list(s)
            i = len(digits) - 1
            while digits[i] == '0':
                digits[i] = '9'
                i -= 1
            digits[i] = str(int(digits[i]) - 1)
            return ''.join(digits).lstrip('0') or '0'
        
        def count_up_to(s, base):
            if s == "0":
                return 0
            digits = to_base(s, base)
            n = len(digits)
            memo = {}
            
            def dp(pos, last_digit, tight, started):
                if pos == n:
                    return 1 if started else 0
                key = (pos, last_digit, tight, started)
                if key in memo:
                    return memo[key]
                upper = digits[pos] if tight else base - 1
                result = 0
                for d in range(upper + 1):
                    if not started:
                        if d == 0:
                            result += dp(pos + 1, 0, tight and d == digits[pos], False)
                        else:
                            result += dp(pos + 1, d, tight and d == digits[pos], True)
                    else:
                        if d >= last_digit:
                            result += dp(pos + 1, d, tight and d == digits[pos], True)
                    result %= MOD
                memo[key] = result
                return result
            
            return dp(0, 0, True, False)
        
        count_r = count_up_to(r, b)
        l_minus_1 = subtract_one(l)
        count_l_minus_1 = count_up_to(l_minus_1, b)
        return (count_r - count_l_minus_1 + MOD) % MOD
# @lc code=end