#
# @lc app=leetcode id=3504 lang=python3
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # Longest palindrome starting at each index in s
        f = [0] * (n + 1)
        pal_s = [[False] * (n + 1) for _ in range(n + 1)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length
                if length == 1:
                    pal_s[i][j] = True
                elif length == 2:
                    pal_s[i][j] = (s[i] == s[j-1])
                else:
                    pal_s[i][j] = (s[i] == s[j-1] and pal_s[i+1][j-1])
                if pal_s[i][j]:
                    f[i] = max(f[i], length)
        
        # Longest palindrome ending at each index in t
        g = [0] * (m + 1)
        pal_t = [[False] * (m + 1) for _ in range(m + 1)]
        for length in range(1, m + 1):
            for i in range(m - length + 1):
                j = i + length
                if length == 1:
                    pal_t[i][j] = True
                elif length == 2:
                    pal_t[i][j] = (t[i] == t[j-1])
                else:
                    pal_t[i][j] = (t[i] == t[j-1] and pal_t[i+1][j-1])
                if pal_t[i][j]:
                    g[j] = max(g[j], length)

        ans = max(max(f), max(g))
        
        # Longest Common Prefix of s and reverse of t
        t_rev = t[::-1]
        lcp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t_rev[j]:
                    lcp[i][j] = 1 + lcp[i+1][j+1]
                
                l = lcp[i][j]
                if l > 0:
                    # Case: |S| >= |T|, S = S1 + S2, T = S1^R, S2 is palindrome starting at i+l
                    ans = max(ans, 2 * l + f[i + l])
                    # Case: |T| >= |S|, T = T1 + T2, S = T2^R, T1 is palindrome ending at m-j-l
                    ans = max(ans, 2 * l + g[m - j - l])
        
        return ans
# @lc code=end