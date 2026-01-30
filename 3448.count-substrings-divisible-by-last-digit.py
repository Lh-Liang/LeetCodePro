#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            last_digit = int(s[i])
            if last_digit == 0:
                continue
            mod = 0
            power = 1
            # Traverse backwards for substrings ending at i
            for j in range(i, -1, -1):
                mod = (int(s[j]) * power + mod) % last_digit
                if mod == 0:
                    ans += 1
                power = (power * 10) % last_digit
        return ans
# @lc code=end