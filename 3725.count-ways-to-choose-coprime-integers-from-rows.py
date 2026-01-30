#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        from math import gcd
        MOD = 10**9 + 7
        m, n = len(mat), len(mat[0])
        max_val = 150
        dp = [0] * (max_val + 1)
        for num in mat[0]:
            dp[num] += 1
        for i in range(1, m):
            ndp = [0] * (max_val + 1)
            for prev_g in range(1, max_val + 1):
                if dp[prev_g]:
                    for num in mat[i]:
                        new_g = gcd(prev_g, num)
                        ndp[new_g] = (ndp[new_g] + dp[prev_g]) % MOD
            dp = ndp
        return dp[1] % MOD
# @lc code=end