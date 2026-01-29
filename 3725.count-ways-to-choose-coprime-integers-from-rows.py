#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAXV = 150
        mu = [0] * (MAXV + 1)
        mu[1] = 1
        vis = [False] * (MAXV + 1)
        primes = []
        for i in range(2, MAXV + 1):
            if not vis[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > MAXV:
                    break
                vis[i * p] = True
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]
        ans = 0
        for d in range(1, MAXV + 1):
            if mu[d] == 0:
                continue
            prod = 1
            for row in mat:
                cnt = sum(1 for x in row if x % d == 0)
                prod = (prod * cnt) % MOD
            ans = (ans + (mu[d] * prod % MOD + MOD) % MOD) % MOD
        return ans

# @lc code=end