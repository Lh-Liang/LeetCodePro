#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(x):
            return x == x[::-1]

        m, n = len(s), len(t)
        ans = 1
        # Check all palindromic substrings in s
        for i in range(m):
            for j in range(i, m):
                if is_palindrome(s[i:j+1]):
                    ans = max(ans, j - i + 1)
        # Check all palindromic substrings in t
        for i in range(n):
            for j in range(i, n):
                if is_palindrome(t[i:j+1]):
                    ans = max(ans, j - i + 1)
        # Now check palindromes that cross s and t
        # For all possible suffixes of s and prefixes of t
        for i in range(m):
            for j in range(n):
                l = 0
                while i - l >= 0 and j + l < n and s[i - l] == t[j + l]:
                    l += 1
                # Odd length palindrome centered between s[i] and t[j]
                if l > 0:
                    ans = max(ans, l * 2)
        # For all possible prefixes of s and suffixes of t
        for i in range(m):
            for j in range(n):
                l = 0
                while i + l < m and j - l >= 0 and s[i + l] == t[j - l]:
                    l += 1
                # Odd length palindrome centered between s[i] and t[j]
                if l > 0:
                    ans = max(ans, l * 2)
        return ans
# @lc code=end