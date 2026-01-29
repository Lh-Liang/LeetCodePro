#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        if not s:
            return ""

        def is_consecutive(c1, c2):
            v1, v2 = ord(c1) - ord('a'), ord(c2) - ord('a')
            diff = abs(v1 - v2)
            return diff == 1 or diff == 25

        # can_empty[i][j] is True if substring s[i...j] can be completely removed
        # Using an offset for j to handle empty ranges easily
        can_empty = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            can_empty[i][i] = True # Range of length 0 is emptyable

        for length in range(2, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length
                # Try to pair s[i] with some s[k]
                for k in range(i + 1, j, 2):
                    if is_consecutive(s[i], s[k]) and can_empty[i+1][k] and can_empty[k+1][j]:
                        can_empty[i][j] = True
                        break

        # dp[i] is the lexicographically smallest string from s[i:]
        dp = [""] * (n + 1)
        for i in range(n - 1, -1, -1):
            # Case 1: Keep the current character
            best = s[i] + dp[i+1]
            
            # Case 2: Try to remove a prefix starting at i
            for k in range(i + 2, n + 1, 2):
                if can_empty[i][k]:
                    cand = dp[k]
                    if cand < best:
                        best = cand
            
            dp[i] = best

        return dp[0]
# @lc code=end