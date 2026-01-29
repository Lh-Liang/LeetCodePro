#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
from typing import List, Set

class Solution:
    def sieve_of_eratosthenes(self, max_number: int) -> Set[int]:
        is_prime = [True] * (max_number + 1)
        p = 2
        while (p * p <= max_number):
            if (is_prime[p] == True):
                for i in range(p * p, max_number + 1, p):
                    is_prime[i] = False
            p += 1
        prime_set = {p for p in range(2, max_number + 1) if is_prime[p]}
        return prime_set
    
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Prepare a set of all primes up to the maximum possible value in nums.
        max_num_value = 105  # As per constraints
        prime_set = self.sieve_of_eratosthenes(max_num_value)
        
        results = []
        n = len(nums)
        
        # Step 2: Process each query and calculate results after updating nums.
        for idx, val in queries:
            # Update nums[idx] with val as per query instruction.
            nums[idx] = val
            
            # Step 3: Find maximum count of distinct primes after split for current nums state.
            max_distinct_primes = 0
            for k in range(1, n):
                prefix_primes = set()
                suffix_primes = set()
                
                # Collect primes from prefix part nums[0..k-1]
                for i in range(k):
                    if nums[i] in prime_set:
                        prefix_primes.add(nums[i])
                
                # Collect primes from suffix part nums[k..end]
                for i in range(k, n):
                    if nums[i] in prime_set:
                        suffix_primes.add(nums[i])
                
                # Calculate total distinct primes count
                total_distinct_primes = len(prefix_primes) + len(suffix_primes)
                max_distinct_primes = max(max_distinct_primes, total_distinct_primes)
            
            # Record result for this query
            results.append(max_distinct_primes)
        
        return results
# @lc code=end