#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def expand_around_center(left, right, str1, str2):
            max_len = 0
            while left >= 0 and right < len(str2) and str1[left] == str2[right]:
                max_len = max(max_len, right - left + 1)
                left -= 1
                right += 1
            return max_len
        
        max_length = 0
        # Check all centers in s concatenated with t reversed (to exploit symmetry)
        for i in range(len(s)):
            for j in range(len(t)):
                # Expand around center between s[i] and t[j]
                max_length = max(max_length, expand_around_center(i, len(t) - j - 1, s, t[::-1]))
                # Expand around center between s[i:i+2] and t[j:j+2], if valid (even length palindromes)
                if i + 1 < len(s) and j + 1 < len(t):
                    max_length = max(max_length, expand_around_center(i + 1, len(t) - j - 2, s[:i+2], t[::-1][j:j+2]))
        return max_length
# @lc code=end