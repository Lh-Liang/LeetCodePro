#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
import math
from collections import defaultdict

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        if maxC >= n:
            return 0
        
        # Precompute primes up to 31622
        limit = 31623
        primes = []
        is_prime = [True] * limit
        for p in range(2, limit):
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, limit, p):
                    is_prime[i] = False

        # Factorize unique numbers and store their indices
        prime_to_indices = defaultdict(list)
        unique_factors = {}
        for i, x in enumerate(nums):
            if x not in unique_factors:
                f = []
                temp = x
                for p in primes:
                    if p * p > temp: break
                    if temp % p == 0:
                        f.append(p)
                        while temp % p == 0: temp //= p
                if temp > 1: f.append(temp)
                unique_factors[x] = f
            for p in unique_factors[x]:
                prime_to_indices[p].append(i)

        # Extract maximal runs for all primes
        maximal_runs = []
        for p in prime_to_indices:
            indices = prime_to_indices[p]
            if not indices: continue
            start = indices[0]
            for j in range(1, len(indices)):
                if indices[j] != indices[j-1] + 1:
                    maximal_runs.append((start, indices[j-1]))
                    start = indices[j]
            maximal_runs.append((start, indices[-1]))

        def can_achieve(L):
            if L == 0:
                return sum(1 for x in nums if x >= 2) <= maxC
            
            # Collect intervals [s, e-L] where GCD >= 2 for length L+1
            k_intervals = []
            for s, e in maximal_runs:
                if e - s + 1 >= L + 1:
                    k_intervals.append((s, e - L))
            
            if not k_intervals: return True
            
            # Merge intervals
            k_intervals.sort()
            merged = []
            if k_intervals:
                curr_s, curr_e = k_intervals[0]
                for i in range(1, len(k_intervals)):
                    s, e = k_intervals[i]
                    if s <= curr_e:
                        curr_e = max(curr_e, e)
                    else:
                        merged.append((curr_s, curr_e))
                        curr_s, curr_e = s, e
                merged.append((curr_s, curr_e))
            
            # Greedy strategy to cover merged intervals
            count = 0
            last_hit = -1
            for S, E in merged:
                k = max(S, last_hit + 1)
                if k <= E:
                    num = (E - k) // (L + 1) + 1
                    count += num
                    last_hit = k + num * (L + 1) - 1
            return count <= maxC

        # Binary search for the minimum stability factor L
        low, high = 0, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
# @lc code=end