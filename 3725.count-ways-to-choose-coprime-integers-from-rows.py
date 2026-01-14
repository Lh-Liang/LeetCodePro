#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#
# @lc code=start
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Find the maximum value in the matrix
        max_val = max(max(row) for row in mat)
        
        # Compute Möbius function using sieve
        mu = [0] * (max_val + 1)
        mu[1] = 1
        smallest_prime_factor = [0] * (max_val + 1)
        
        # Sieve to find smallest prime factor
        for i in range(2, max_val + 1):
            if smallest_prime_factor[i] == 0:  # i is prime
                smallest_prime_factor[i] = i
                for j in range(i, max_val + 1, i):
                    if smallest_prime_factor[j] == 0:
                        smallest_prime_factor[j] = i
        
        # Compute Möbius function
        for i in range(2, max_val + 1):
            p = smallest_prime_factor[i]
            if smallest_prime_factor[i // p] == p:
                # i has p^2 as a factor
                mu[i] = 0
            else:
                mu[i] = -mu[i // p]
        
        # Apply Möbius inversion
        result = 0
        for d in range(1, max_val + 1):
            if mu[d] == 0:
                continue
            
            # Count ways where all chosen numbers are divisible by d
            ways = 1
            for row in mat:
                count = sum(1 for x in row if x % d == 0)
                ways = (ways * count) % MOD
            
            result = (result + mu[d] * ways) % MOD
        
        return result
# @lc code=end