#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(mat)
        n = len(mat[0])
        max_val = 150
        
        # Precompute frequencies of each number in each row
        row_counts = [[0] * (max_val + 1) for _ in range(m)]
        for i in range(m):
            for val in mat[i]:
                row_counts[i][val] += 1
        
        # Mobius function calculation up to 150
        mu = [0] * (max_val + 1)
        mu[1] = 1
        primes = []
        is_prime = [True] * (max_val + 1)
        for i in range(2, max_val + 1):
            if is_prime[i]:
                primes.append(i)
                mu[i] = -1
            for p in primes:
                if i * p > max_val: break
                is_prime[i * p] = False
                if i % p == 0:
                    mu[i * p] = 0
                    break
                else:
                    mu[i * p] = -mu[i]
        
        ans = 0
        for g in range(1, max_val + 1):
            if mu[g] == 0: continue
            
            # Calculate f(g): number of ways such that GCD is multiple of g
            ways_g = 1
            for i in range(m):
                count_divisible = 0
                for multiple in range(g, max_val + 1, g):
                    count_divisible += row_counts[i][multiple]
                
                ways_g = (ways_g * count_divisible) % MOD
                if ways_g == 0: break
            
            if mu[g] == 1:
                ans = (ans + ways_g) % MOD
            else:
                ans = (ans - ways_g + MOD) % MOD
                
        return ans
# @lc code=end