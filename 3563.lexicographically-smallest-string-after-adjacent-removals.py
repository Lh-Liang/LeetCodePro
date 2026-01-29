#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        # is_removable[i][j] indicates if the substring s[i...j] can be completely removed.
        # We use a table of size (n+1)x(n+1) to handle base cases easily.
        is_removable = [[False] * (n + 1) for _ in range(n + 1)]
        
        # Base case: An empty range (where end < start) is considered removable.
        for i in range(n + 1):
            is_removable[i][i-1] = True
            
        def is_consecutive(c1, c2):
            diff = abs(ord(c1) - ord(c2))
            return diff == 1 or diff == 25
            
        # Stage 1: Interval DP to find all removable substrings in O(N^3).
        for length in range(2, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length - 1
                # Check if endpoints s[i] and s[j] can be paired after removing the interior.
                if is_consecutive(s[i], s[j]) and is_removable[i+1][j-1]:
                    is_removable[i][j] = True
                else:
                    # Check if the substring can be split into two smaller removable blocks.
                    for k in range(i + 1, j, 2):
                        if is_removable[i][k] and is_removable[k+1][j]:
                            is_removable[i][j] = True
                            break
                            
        # Stage 2: Suffix DP to find the lexicographically smallest result in O(N^3).
        # dp[i] stores the smallest string obtainable from s[i...n-1].
        dp = [""] * (n + 1)
        for i in range(n - 1, -1, -1):
            # Option 1: Keep the current character s[i].
            res = s[i] + dp[i+1]
            
            # Option 2: Remove s[i] by pairing it with some s[k].
            # This is possible only if the entire block s[i...k] is removable.
            for k in range(i + 1, n, 2):
                if is_removable[i][k]:
                    candidate = dp[k+1]
                    if candidate < res:
                        res = candidate
            dp[i] = res
            
        return dp[0]
# @lc code=end