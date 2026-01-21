#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
import math
from typing import List

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        if maxC >= n:
            return 0
        
        # Find all maximal blocks [a, b] where every element is divisible by some prime p
        # First, collect all prime factors for each number
        prime_to_indices = {}
        max_val = 0
        for x in nums:
            if x > max_val: max_val = x
            
        limit = int(math.sqrt(max_val)) + 1
        primes = []
        is_prime = [True] * (limit + 1)
        for p in range(2, limit + 1):
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
                    
        for i, x in enumerate(nums):
            temp = x
            for p in primes:
                if p * p > temp: break
                if temp % p == 0:
                    if p not in prime_to_indices:
                        prime_to_indices[p] = []
                    prime_to_indices[p].append(i)
                    while temp % p == 0:
                        temp //= p
            if temp > 1:
                if temp not in prime_to_indices:
                    prime_to_indices[temp] = []
                prime_to_indices[temp].append(i)
        
        # E[i] = max end index of a stable block starting at or before i
        E = [i for i in range(n)]
        for p in prime_to_indices:
            indices = prime_to_indices[p]
            if not indices: continue
            start = indices[0]
            for idx in range(1, len(indices)):
                if indices[idx] != indices[idx-1] + 1:
                    E[start] = max(E[start], indices[idx-1])
                    start = indices[idx]
            E[start] = max(E[start], indices[-1])
            
        for i in range(1, n):
            if E[i-1] > E[i]:
                E[i] = E[i-1]
        
        def check(k):
            if k == 0: return True # Should not happen given constraints
            count = 0
            curr = 0
            while curr <= n - k:
                # Find first j >= curr such that E[j] >= j + k - 1
                # Since E[j] is non-decreasing, we can check sequentially
                if E[curr] >= curr + k - 1:
                    count += 1
                    curr += k
                else:
                    curr += 1
                if count > maxC: return False
            return count <= maxC

        # Binary search for minimum stability factor L
        low = 0
        high = n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            # Stability factor mid means no stable subarray of length mid + 1
            if check(mid + 1):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# @lc code=end