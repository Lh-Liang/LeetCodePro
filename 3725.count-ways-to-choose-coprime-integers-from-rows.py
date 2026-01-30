#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
from typing import List
from math import gcd
from collections import Counter

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(mat)
        maxv = 150
        # dp[g]: number of ways to pick from processed rows so that GCD is exactly g
        count = Counter(mat[0])
        dp = [0] * (maxv + 1)
        for v in count:
            dp[v] = count[v]
        for i in range(1, m):
            ndp = [0] * (maxv + 1)
            cur_count = Counter(mat[i])
            for g in range(1, maxv + 1):
                if dp[g] == 0:
                    continue
                for v in cur_count:
                    ng = gcd(g, v)
                    ndp[ng] = (ndp[ng] + dp[g] * cur_count[v]) % MOD
            dp = ndp
        # Ensure the result corresponds to the count of ways with GCD 1
        return dp[1]
# @lc code=end