#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
from typing import List
import math

class Solution:
    def sieve_of_eratosthenes(self, max_num: int) -> List[bool]:
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if (is_prime[p] == True):
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False # 0 and 1 are not primes
        return is_prime
    
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        max_val = 105 # Given constraint on nums[i]
        is_prime = self.sieve_of_eratosthenes(max_val)
        results = []
        n = len(nums)
        
        def count_distinct_primes(nums_segment):
            prime_set = set()
            for num in nums_segment:
                if is_prime[num]:
                    prime_set.add(num)
            return len(prime_set)

        for idx, val in queries:
            nums[idx] = val
            prefix_primes = [0]* (n+1) # Store count of distinct primes up to index i for prefix
            suffix_primes = [0]* (n+1) # Store count of distinct primes from index i to end for suffix
            
            # Calculate prefix primes count array 
            current_primes = set()
            for i in range(n):
                if is_prime[nums[i]]:
                    current_primes.add(nums[i])
                prefix_primes[i+1] = len(current_primes)
                
            # Calculate suffix primes count array 
            current_primes.clear()
            for i in range(n-1, -1, -1):
                if is_prime[nums[i]]:
                    current_primes.add(nums[i])
                suffix_primes[i] = len(current_primes)
                
            max_primes = 0
            for k in range(1, n):
                max_primes = max(max_primes, prefix_primes[k] + suffix_primes[k])
                
            results.append(max_primes)
        
        return results
# @lc code=end