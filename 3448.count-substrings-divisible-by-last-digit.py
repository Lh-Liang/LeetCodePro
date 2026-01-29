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
        
        # Iterate over each starting point for substrings
        for start in range(n):
            # Form substrings from `start` to `end`
            for end in range(start, n):
                # Current substring's last digit
                last_digit = int(s[end])
                if last_digit != 0: # Check if last digit is non-zero
                    # Convert substring to integer and check divisibility
                    if int(s[start:end+1]) % last_digit == 0:
                        count += 1
        return count
# @lc code=end