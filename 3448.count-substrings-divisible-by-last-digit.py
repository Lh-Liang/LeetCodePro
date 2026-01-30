#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            last_digit = int(s[i])
            if last_digit == 0:
                continue  # Skip substrings ending in 0 as they cannot be valid divisors
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])   # Form the number represented by s[i:j+1]
                if num % last_digit == 0:
                    count += 1               # Count this substring if it is divisible by its last digit
        return count
# @lc code=end