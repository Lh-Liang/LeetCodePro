#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
from math import gcd
from collections import defaultdict

MOD = int(1e9 + 7)

class Solution:
    def countCoprime(self, mat):
        m = len(mat)
        n = len(mat[0])
        
        # Initialize DP table
        dp = [defaultdict(int) for _ in range(m + 1)]
        dp[0][0] = 1 # base case: choosing nothing has gcd of zero (neutral element)
        
        # Iterate over each row in matrix
        for i in range(m):
            for num in mat[i]:
                for g, count in list(dp[i].items()):
                    new_gcd = gcd(g, num)
                    dp[i + 1][new_gcd] = (dp[i + 1][new_gcd] + count) % MOD
        
        return dp[m][1]
# @lc code=end