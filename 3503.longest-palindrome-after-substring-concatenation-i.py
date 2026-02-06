#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(x):
            return x == x[::-1]
        max_len = 0
        # Checking all concatenations of substrings from s and t
        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                # Concatenate substrings s[:i] with t[j:]
                candidate = s[:i] + t[j:]
                if is_palindrome(candidate):
                    max_len = max(max_len, len(candidate))
                # Concatenate substrings t[:j] with s[i:]
                candidate = t[:j] + s[i:]
                if is_palindrome(candidate):
                    max_len = max(max_len, len(candidate))
        return max_len
# @lc code=end