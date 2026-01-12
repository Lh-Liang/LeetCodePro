#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        # is_empty[i][j] will be true if s[i:j+1] can be completely removed
        is_empty = [[False] * n for _ in range(n)]
        
        def are_consecutive(c1, c2):
            v1, v2 = ord(c1) - ord('a'), ord(c2) - ord('a')
            return (v1 + 1) % 26 == v2 or (v2 + 1) % 26 == v1

        # Interval DP to find all reducible substrings
        for length in range(2, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length - 1
                # Case 1: s[i] and s[j] are consecutive and the middle is reducible
                if are_consecutive(s[i], s[j]):
                    if length == 2 or is_empty[i + 1][j - 1]:
                        is_empty[i][j] = True
                # Case 2: Substring can be split into two reducible parts
                if not is_empty[i][j]:
                    for k in range(i + 1, j, 2):
                        if is_empty[i][k] and is_empty[k + 1][j]:
                            is_empty[i][j] = True
                            break
        
        # DP to find the lexicographically smallest string
        # dp[i] = smallest string using characters from s[0...i-1]
        dp = ["" for _ in range(n + 1)]
        for i in range(1, n + 1):
            # Option 1: Keep the current character s[i-1]
            res = dp[i-1] + s[i-1]
            # Option 2: Try to remove a suffix s[j...i-1]
            for j in range(i - 1):
                if is_empty[j][i-1]:
                    if dp[j] < res:
                        res = dp[j]
            # Special case: if the entire prefix s[0...i-1] is reducible
            if is_empty[0][i-1]:
                if "" < res:
                    res = ""
            dp[i] = res
            
        return dp[n]
# @lc code=end