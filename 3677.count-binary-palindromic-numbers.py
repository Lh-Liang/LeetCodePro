#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        count = 0
        for k in range(n + 1):
            if is_palindrome(bin(k)[2:]):
                count += 1
        return count
# @lc code=end