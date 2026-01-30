#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(s):
            return s == s[::-1]
        max_length = 0
        # Check all possible substrings of s
        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                subs_s = s[i:j]
                # Check all possible substrings of t
                for k in range(len(t) + 1):
                    for l in range(k, len(t) + 1):
                        subs_t = t[k:l]
                        combined = subs_s + subs_t
                        if is_palindrome(combined):
                            max_length = max(max_length, len(combined))
        return max_length
# @lc code=end