#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for j in range(n):
            last_digit = int(s[j])
            if last_digit == 0:
                continue
            mod = 0
            power = 1
            # Check all substrings ending at j
            for i in range(j, -1, -1):
                mod = (int(s[i]) * power + mod) % last_digit
                if mod == 0:
                    res += 1
                power = (power * 10) % last_digit
        return res
# @lc code=end