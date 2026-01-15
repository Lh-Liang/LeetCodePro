#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
from typing import List
from math import gcd
from collections import defaultdict, Counter

MOD = 10**9 + 7

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        # Step 1: Precompute frequency of each integer in each row.
        # Since n <= 150 and numbers <= 150, we can represent each row as a counter of frequencies.
        rows = []
        for r in mat:
            cnt = Counter(r)
            rows.append(cnt)
        
        m = len(mat)
        # The maximum value in mat is at most 150.
        max_val = 150
        
        # Step 2: Use inclusion-exclusion principle via Möbius function.
        # Let f(d) be number of ways to choose numbers such that gcd is a multiple of d.
        # Then by inclusion-exclusion, the number of ways with gcd exactly 1 is sum_{d>=1} mu(d) * f(d).
        # But we can compute using Möbius inversion: answer = sum_{d=1}^{max_val} mu(d) * F(d),
        # where F(d) = product over rows of (count of numbers divisible by d in that row).
        
        # Precompute Möbius function for numbers up to max_val.
        mu = [1] * (max_val + 1)
        primes = []
        is_prime = [True] * (max_val + 1)
        for i in range(2, max_val + 1):
            if is_prime[i]:
                primes.append(i)
                mu[i] = -1   # i is prime -> mu(i) = -1
            for p in primes:
                if i * p > max_val:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    mu[i * p] = 0   # square factor
                    break
                else:
                    mu[i * p] = -mu[i]
        
        # For each row, precompute count_divisible[d] for d from 1 to max_val.
        row_div_counts = []
        for cnt in rows:
            div_count = [0] * (max_val + 1)
            for num, freq in cnt.items():
                # For each divisor of num? Actually we need for each d, how many numbers are divisible by d.
                # Since numbers are small, we can iterate divisors of each number.
                # But there are at most 150 numbers per row and each number <=150, so we can compute divisors naively.
                divisors = self.get_divisors(num)
                for d in divisors:
                    div_count[d] += freq
            row_div_counts.append(div_count)
        
        ans = 0
        for d in range(1, max_val + 1):
            if mu[d] == 0:
                continue
            ways = 1
            for i in range(m):
                ways = (ways * row_div_counts[i][d]) % MOD
            ans = (ans + mu[d] * ways) % MOD
        return ans % MOD
    
def get_divisors(self, n: int) -> List[int]:
divisors = []
i = 1while i*i <= n:if n % i == 0:divisors.append(i)if i != n // i:divisors.append(n // i)i += 1return divisors