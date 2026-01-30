#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution:
    def specialPalindrome(self, n: int) -> int:
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        
        def is_special(x):
            from collections import Counter
            freq = Counter(str(x))
            for digit, count in freq.items():
                if int(digit) != count:
                    return False
            return True
        
        num = n + 1
        while True:
            if is_palindrome(num) and is_special(num):
                return num
            num += 1
# @lc code=end