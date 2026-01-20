#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

from typing import List

# @lc code=start
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAX = 150
        m = len(mat)
        
        # Precompute frequency for each row
        freq = [[0] * (MAX + 1) for _ in range(m)]
        for r in range(m):
            for x in mat[r]:
                freq[r][x] += 1
        
        # Compute Möbius function
        mu = [0] * (MAX + 1)
        vis = [False] * (MAX + 1)
        mu[1] = 1
        primes = []
        for i in range(2, MAX + 1):
            if not vis[i]:
                primes.append(i)
                mu[i] = -1
            for j in range(len(primes)):
                p = primes[j]
                if i * p > MAX:
                    break
                vis[i * p] = True
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]
        
        # Compute sum mu[d] * H(d)
        ans = 0
        for d in range(1, MAX + 1):
            if mu[d] == 0:
                continue
            prod = 1
            for r in range(m):
                cnt = 0
                mul = d
                while mul <= MAX:
                    cnt += freq[r][mul]
                    mul += d
                prod = (prod * cnt) % MOD
            ans = (ans + mu[d] * prod) % MOD
        
        return (ans + MOD) % MOD

# @lc code=end
