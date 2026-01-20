#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
import sys

# Increase recursion depth for deep DP trees
sys.setrecursionlimit(20000)

class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        
        # Memoization tables
        memo_removable = {}
        memo_solve = {}

        def are_consecutive(c1, c2):
            diff = abs(ord(c1) - ord(c2))
            return diff == 1 or diff == 25

        def can_fully_remove(i, j):
            if i > j:
                return True
            if (i, j) in memo_removable:
                return memo_removable[(i, j)]
            
            # If length is odd, cannot remove all pairs
            if (j - i + 1) % 2 != 0:
                memo_removable[(i, j)] = False
                return False
            
            res = False
            # Try to pair s[i] with s[k]
            # For s[i] and s[k] to be removed together, s[i+1...k-1] must be fully removable
            # and s[k+1...j] must be fully removable.
            # We iterate k with step 2 because the inner chunk size must be even.
            for k in range(i + 1, j + 1, 2):
                if are_consecutive(s[i], s[k]):
                    if can_fully_remove(i + 1, k - 1) and can_fully_remove(k + 1, j):
                        res = True
                        break
            
            memo_removable[(i, j)] = res
            return res

        def solve(i, j):
            if i > j:
                return ""
            if (i, j) in memo_solve:
                return memo_solve[(i, j)]
            
            # Option 1: Keep s[i]
            # We just append the best result for the rest of the string
            res = s[i] + solve(i + 1, j)
            
            # Option 2: Try to remove s[i] by pairing with some s[k]
            # s[i] can be removed with s[k] if they are consecutive
            # AND everything between them (s[i+1...k-1]) can be fully removed.
            # If that happens, we are left with the problem of solving s[k+1...j].
            for k in range(i + 1, j + 1):
                if are_consecutive(s[i], s[k]):
                    # Check if the middle part is removable
                    if can_fully_remove(i + 1, k - 1):
                        candidate = solve(k + 1, j)
                        if candidate < res:
                            res = candidate
            
            memo_solve[(i, j)] = res
            return res

        return solve(0, n - 1)

# @lc code=end