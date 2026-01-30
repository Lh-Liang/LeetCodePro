#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
from typing import List
class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Sieve of Eratosthenes to identify all primes up to 10^5
        MAX_N = 10**5 + 1
        is_prime = [False, False] + [True] * (MAX_N - 2)
        for i in range(2, int(MAX_N ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_N, i):
                    is_prime[j] = False
        results = []
        n = len(nums)
        for idx, val in queries:
            nums[idx] = val
            # Compute prefix and suffix sets of distinct primes
            prefix = [set() for _ in range(n+1)]
            suffix = [set() for _ in range(n+1)]
            for i in range(1, n+1):
                prefix[i] = set(prefix[i-1])
                if is_prime[nums[i-1]]:
                    prefix[i].add(nums[i-1])
            for i in range(n-1, -1, -1):
                suffix[i] = set(suffix[i+1])
                if is_prime[nums[i]]:
                    suffix[i].add(nums[i])
            max_total = 0
            for k in range(1, n):
                total = len(prefix[k]) + len(suffix[k])
                max_total = max(max_total, total)
            results.append(max_total)
        return results
# @lc code=end