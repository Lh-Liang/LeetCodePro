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
        # Iterate over all possible end indices of substrings
        for end in range(n):
            last_digit = int(s[end])
            if last_digit == 0:
                continue  # Skip if last digit is zero, as no divisibility possible
            # Initialize current number starting from s[end] as a single digit number
            num = 0
            # Extend the substring backwards checking divisibility by last_digit
            for start in range(end, -1, -1):
                num = num + int(s[start]) * (10 ** (end - start))  # Update number ending at 'end' starting from 'start'
                if num % last_digit == 0:
                    count += 1  # If divisible, increment count
        return count  # Return total count of such substrings
# @lc code=end