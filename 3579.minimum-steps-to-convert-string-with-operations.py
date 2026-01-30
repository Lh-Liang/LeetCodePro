#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][i] = 0  # Empty substring needs 0 ops

        for length in range(1, n+1):
            for l in range(n-length+1):
                r = l + length
                # If substrings are equal, no op needed
                if word1[l:r] == word2[l:r]:
                    dp[l][r] = 0
                    continue
                # 1. Reverse
                if word1[l:r][::-1] == word2[l:r]:
                    dp[l][r] = min(dp[l][r], 1)
                # 2. Swap any two chars
                s1 = list(word1[l:r])
                s2 = word2[l:r]
                m = r - l
                found_swap = False
                for i in range(m):
                    for j in range(i+1, m):
                        s1[i], s1[j] = s1[j], s1[i]
                        if ''.join(s1) == s2:
                            dp[l][r] = min(dp[l][r], 1)
                            found_swap = True
                        s1[i], s1[j] = s1[j], s1[i]
                    if found_swap: break
                # 3. Replace a single char
                for i in range(m):
                    if word1[l+i] != word2[l+i]:
                        s1 = list(word1[l:r])
                        s1[i] = word2[l+i]
                        if ''.join(s1) == s2:
                            dp[l][r] = min(dp[l][r], 1)
                            break
                # 4. Split into two and combine
                for mid in range(l+1, r):
                    dp[l][r] = min(dp[l][r], dp[l][mid] + dp[mid][r])
        return dp[0][n]
# @lc code=end