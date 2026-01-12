#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if m == 0:
            return 0
        
        # Find the maximum value in the matrix to define our range
        V = 0
        for row in mat:
            for val in row:
                if val > V:
                    V = val
        
        # Precompute Möbius function up to V
        # mu[n] = 1 if n=1, (-1)^k if n is product of k distinct primes, 0 if n has a square factor
        mu = [0] * (V + 1)
        mu[1] = 1
        for i in range(1, V + 1):
            for j in range(2 * i, V + 1, i):
                mu[j] -= mu[i]
        
        # Precompute the number of elements in each row that are multiples of g
        # First, count occurrences of each value in each row
        row_counts = [[0] * (V + 1) for _ in range(m)]
        for r in range(m):
            for val in mat[r]:
                row_counts[r][val] += 1
        
        # row_g_counts[r][g] will store how many elements in row r are divisible by g
        row_g_counts = [[0] * (V + 1) for _ in range(m)]
        for r in range(m):
            for g in range(1, V + 1):
                count = 0
                for multiple in range(g, V + 1, g):
                    count += row_counts[r][multiple]
                row_g_counts[r][g] = count
        
        MOD = 10**9 + 7
        ans = 0
        
        # Apply the inclusion-exclusion formula: 
        # Number of ways with GCD 1 = sum_{g=1 to V} mu(g) * f(g)
        # where f(g) is the number of ways to pick one multiple of g from each row.
        for g in range(1, V + 1):
            if mu[g] == 0:
                continue
            
            # Calculate f(g) = product of (number of multiples of g in row r) across all rows
            prod = 1
            for r in range(m):
                prod = (prod * row_g_counts[r][g]) % MOD
                if prod == 0:
                    break
            
            if mu[g] == 1:
                ans = (ans + prod) % MOD
            else: # mu[g] == -1
                ans = (ans - prod + MOD) % MOD
                
        return ans
# @lc code=end