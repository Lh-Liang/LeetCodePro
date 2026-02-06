#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        def longest_palindrome_substring(s):
            max_len = 0
            start = 0
            for i in range(len(s)):
                len1 = expand_around_center(s, i, i)
                len2 = expand_around_center(s, i, i + 1)
                max_len = max(max_len, len1, len2)
            return max_len
        
        # Calculate longest palindromic substring lengths for both s and t individually
        max_s = longest_palindrome_substring(s)
        max_t = longest_palindrome_substring(t)
        
        # Try concatenating palindromic parts from s and t
        def concat_palindrome_max_length(s, t):
            total_max = 0
            # Attempt all combinations of substrings from s and t as potential centers for palindrome formation
            for i in range(len(s)):
                for j in range(len(t)):
                    if s[i] == t[j]:
                        l, r = i, j + len(s)
                        while l >= 0 and r < len(s) + len(t) and (
s[l] == t[r - len(s)] if r >= len(s) else s[l] == s[r]):
                            l -= 1
                            r += 1
                        total_max = max(total_max, r - l - 1)
            return total_max
        
        # The result is the maximum length found through individual or concatenated palindromes.
        return max(max_s, max_t, concat_palindrome_max_length(s, t))
# @lc code=end