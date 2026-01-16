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
        
        # For each possible substring s[i:j+1]
        for i in range(n):
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])
                last_digit = int(s[j])
                if last_digit != 0 and num % last_digit == 0:
                    count += 1
        return count
# @lc code=end