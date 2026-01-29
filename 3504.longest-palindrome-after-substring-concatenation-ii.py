#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # Helper function to check if a string is a palindrome
        def is_palindrome(x):
            return x == x[::-1]
        
        # Initialize maximum length of palindrome found
        max_length = 0
        
        # Consider all possible substrings of s and t
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                s_sub = s[i:j]
                for k in range(len(t)):
                    for l in range(k + 1, len(t) + 1):
                        t_sub = t[k:l]
                        combined = s_sub + t_sub
                        if is_palindrome(combined):
                            max_length = max(max_length, len(combined))
        return max_length
# @lc code=end