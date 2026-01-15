#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        def consecutive(c1, c2):
            diff = abs(ord(c1) - ord(c2))
            return diff == 1 or diff == 25
        
        # Build canRemove table: canRemove[i][j] is True if s[i:j+1] can be completely removed
        canRemove = [[False] * n for _ in range(n)]
        
        for length in range(2, n + 1, 2):  # Only even lengths can be fully removed
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i + 1, j + 1, 2):  # k-i must be odd
                    if consecutive(s[i], s[k]):
                        left_ok = (k == i + 1) or canRemove[i + 1][k - 1]
                        right_ok = (k == j) or canRemove[k + 1][j]
                        if left_ok and right_ok:
                            canRemove[i][j] = True
                            break
        
        # Memoized DP for finding the lexicographically smallest string
        memo = {}
        
        def dp(i, j):
            if j < i:
                return ""
            if (i, j) in memo:
                return memo[(i, j)]
            
            candidates = []
            
            # Option 1: Remove the entire substring (if possible)
            if canRemove[i][j]:
                candidates.append("")
            
            # Option 2: Keep s[k] as the first character and optimally process the rest
            for k in range(i, j + 1):
                if k == i or canRemove[i][k - 1]:
                    rest = dp(k + 1, j)
                    candidates.append(s[k] + rest)
            
            result = min(candidates)
            memo[(i, j)] = result
            return result
        
        return dp(0, n - 1)
# @lc code=end