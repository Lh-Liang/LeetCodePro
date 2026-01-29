#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
from math import gcd
from collections import defaultdict
from typing import List

MOD = 10**9 + 7

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # Initialize DP table with default dictionaries for automatic zero handling.
        dp = [defaultdict(int) for _ in range(m)]
        
        # Base case for the first row.
        for num in mat[0]:
            dp[0][num] += 1
            
        # Fill DP table for each subsequent row.
        for i in range(1, m):
            for num in mat[i]:
                for g, count in dp[i-1].items():
                    new_gcd = gcd(g, num)
                    dp[i][new_gcd] = (dp[i][new_gcd] + count) % MOD
                    
        # The number of ways such that GCD is 1 after using all rows.
        return dp[m-1][1]
# @lc code=end