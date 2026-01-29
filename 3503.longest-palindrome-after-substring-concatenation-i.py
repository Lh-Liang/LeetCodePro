#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        ans = 0
        
        # Case 1: Core is in t. 
        # Substring of t is B = X + Y, where X is a palindrome.
        # If Y^R is a substring in s, we can form the palindrome Y^R + X + Y.
        for i in range(m):
            for j in range(i, m):
                B = t[i:j+1]
                for k in range(len(B) + 1):
                    X = B[:k]  # Potential palindromic core
                    if X == X[::-1]:
                        Y = B[k:]
                        # Check if the reverse of the suffix Y exists in s
                        if Y[::-1] in s:
                            ans = max(ans, 2 * len(Y) + len(X))
                            
        # Case 2: Core is in s.
        # Substring of s is A = X + Y, where Y is a palindrome.
        # If X^R is a substring in t, we can form the palindrome X + Y + X^R.
        for i in range(n):
            for j in range(i, n):
                A = s[i:j+1]
                for k in range(len(A) + 1):
                    Y = A[k:]  # Potential palindromic core
                    if Y == Y[::-1]:
                        X = A[:k]
                        # Check if the reverse of the prefix X exists in t
                        if X[::-1] in t:
                            ans = max(ans, 2 * len(X) + len(Y))
                            
        return ans
# @lc code=end