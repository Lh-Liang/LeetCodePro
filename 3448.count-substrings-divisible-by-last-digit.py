#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        # Iterate over every possible end position of a substring
        for end in range(n):
            last_digit = int(s[end])
            if last_digit == 0:
                continue  # Cannot divide by zero
            # Check all substrings ending at `end`
            num = 0
            for start in range(end, -1, -1):
                num = num + int(s[start]) * (10 ** (end - start)) 
                if num % last_digit == 0:
                    count += 1
        return count
# @lc code=end