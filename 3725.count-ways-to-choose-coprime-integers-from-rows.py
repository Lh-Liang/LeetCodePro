#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        M = len(mat)
        MAX_VAL = 150

        # Precompute Mobius function up to 150 using a simple sieve
        mu = [0] * (MAX_VAL + 1)
        mu[1] = 1
        primes = []
        is_prime = [True] * (MAX_VAL + 1)
        for i in range(2, MAX_VAL + 1):
            if is_prime[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > MAX_VAL:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]

        # Precompute frequencies for each row to speed up f(d) calculation
        row_counts = []
        for row in mat:
            counts = [0] * (MAX_VAL + 1)
            for val in row:
                counts[val] += 1
            row_counts.append(counts)

        total_ways = 0
        for d in range(1, MAX_VAL + 1):
            if mu[d] == 0:
                continue
            
            # Calculate f(d): ways to pick multiples of d from every row
            f_d = 1
            for counts in row_counts:
                count_divisible = 0
                for multiple in range(d, MAX_VAL + 1, d):
                    count_divisible += counts[multiple]
                
                f_d = (f_d * count_divisible) % MOD
                if f_d == 0:
                    break
            
            if mu[d] == 1:
                total_ways = (total_ways + f_d) % MOD
            else: # mu[d] == -1
                total_ways = (total_ways - f_d + MOD) % MOD
        
        return total_ways
# @lc code=end