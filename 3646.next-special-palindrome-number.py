#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution:
    def specialPalindrome(self, n: int) -> int:
        def is_palindrome(num):
            s = str(num)
            return s == s[::-1]
        
        def is_special(num):
            from collections import Counter
            s = str(num)
            count = Counter(s)
            for digit in count:
                if int(digit) != count[digit]:
                    return False
            return True
        
        current = n + 1
        while True:
            if is_palindrome(current) and is_special(current):
                return current
            current += 1
# @lc code=end