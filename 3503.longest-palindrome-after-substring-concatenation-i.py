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
        maxlen = 0
        n, m = len(s), len(t)
        # All possible substrings from s
        for i in range(n+1):
            for j in range(i, n+1):
                substr_s = s[i:j]
                # All possible substrings from t
                for k in range(m+1):
                    for l in range(k, m+1):
                        substr_t = t[k:l]
                        candidate = substr_s + substr_t
                        if candidate and is_palindrome(candidate):
                            maxlen = max(maxlen, len(candidate))
        return maxlen
# @lc code=end