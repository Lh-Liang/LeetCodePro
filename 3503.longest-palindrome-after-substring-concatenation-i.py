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
        n, m = len(s), len(t)
        # s_sub + t_sub, t_sub may be empty
        for i in range(n+1):
            for j in range(i, n+1):
                s_sub = s[i:j]
                for p in range(m+1):
                    for q in range(p, m+1):
                        t_sub = t[p:q]
                        concat = s_sub + t_sub
                        if concat and is_palindrome(concat):
                            max_len = max(max_len, len(concat))
        return max_len
# @lc code=end