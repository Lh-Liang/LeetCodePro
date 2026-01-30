#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
from math import gcd
from typing import List

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(mat), len(mat[0])
        
        # Precompute GCD for pairs in range [1, 150]
        gcd_table = [[gcd(i, j) for j in range(151)] for i in range(151)]
        
        # Initialize DP table
dp = [{} for _ in range(m)]
        # Base case for first row
        for num in mat[0]:
            dp[0][num] = dp[0].get(num, 0) + 1
        
        # Fill DP table
        for i in range(1, m):
            for num in mat[i]:
                for g in dp[i-1].keys():
                    new_gcd = gcd_table[g][num]
                    dp[i][new_gcd] = (dp[i].get(new_gcd, 0) + dp[i-1][g]) % MOD
                
                # Also consider starting fresh with current number alone
                dp[i][num] = (dp[i].get(num, 0) + 1) % MOD
        
        # Count ways where final GCD is exactly 1 after processing all rows
        return dp[-1].get(1, 0)
# @lc code=end