#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        max_length = 0
        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                combined = s[:i] + t[:j]
                if is_palindrome(combined):
                    max_length = max(max_length, len(combined))
        return max_length
# @lc code=end