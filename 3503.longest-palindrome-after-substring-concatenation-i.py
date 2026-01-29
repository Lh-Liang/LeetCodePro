#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        max_len = 0
        ns, nt = len(s), len(t)
        for i in range(ns + 1):
            for j in range(i, ns + 1):
                for k in range(nt + 1):
                    for l in range(k, nt + 1):
                        candidate = s[i:j] + t[k:l]
                        if candidate == candidate[::-1]:
                            max_len = max(max_len, len(candidate))
        return max_len

# @lc code=end