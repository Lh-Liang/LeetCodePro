# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        # Initialize variables
        s_len = len(s)
        t_len = len(t)
        max_len = 0
        
        # Helper function to check if a string is a palindrome
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        # Check each possible concatenated substring combination
        for i in range(s_len):
            for j in range(t_len):
                # Get all possible substrings from s[i:] and t[:j+1]
                combined_s_t = s[i:] + t[:j+1]
                combined_t_s = t[j:] + s[:i+1]
                
                # Check if these combinations form palindromes
                if is_palindrome(combined_s_t):
                    max_len = max(max_len, len(combined_s_t))
                if is_palindrome(combined_t_s):
                    max_len = max(max_len, len(combined_t_s))
        
        return max_len
# @lc code=end