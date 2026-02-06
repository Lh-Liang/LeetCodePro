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
                continue
            num = 0
            count += 1
            for j in range(i - 1, -1, -1):
                num = num * 10 + int(s[j])
                if num % last_digit == 0:
                    count += 1
        return count
# @lc code=end