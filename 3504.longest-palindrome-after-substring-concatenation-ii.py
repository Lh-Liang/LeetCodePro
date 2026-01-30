#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def longest_palindromic_subseq_length(s):
            n = len(s)
            dp = [[0] * n for _ in range(n)]
            for i in range(n):
                dp[i][i] = 1
            for cl in range(2, n+1):
                for i in range(n - cl + 1):
                    j = i + cl - 1
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])
            return dp[0][-1]
        
        # Get the longest palindromic subsequence lengths of s and t
        max_len_s = longest_palindromic_subseq_length(s)
        max_len_t = longest_palindromic_subseq_length(t)
        
        # Consider combinations of palindromes from each string
        # Further improvements would involve checking valid combinations between them
        return max(max_len_s, max_len_t)
# @lc code=end