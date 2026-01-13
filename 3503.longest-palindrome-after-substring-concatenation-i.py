#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(string):
            return string == string[::-1]
        
        max_len = 0
        
        # Try all substrings of s
        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                substr_s = s[i:j]
                
                # Try all substrings of t
                for k in range(len(t) + 1):
                    for l in range(k, len(t) + 1):
                        substr_t = t[k:l]
                        
                        # Concatenate and check
                        concat = substr_s + substr_t
                        if is_palindrome(concat):
                            max_len = max(max_len, len(concat))
        
        return max_len
# @lc code=end