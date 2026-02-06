#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Precompute all prime numbers up to 10^5 using Sieve of Eratosthenes
        max_val = 10**5
        is_prime = [True] * (max_val + 1)
        p = 2
        while p * p <= max_val:
            if is_prime[p]:
                for i in range(p * p, max_val + 1, p):
                    is_prime[i] = False
            p += 1
        primes_set = {i for i in range(2, max_val + 1) if is_prime[i]}
        
        results = []
        for idx, val in queries:
            nums[idx] = val # Update nums as per query
            n = len(nums)
            max_distinct_primes = 0
            
            # Calculate prime counts for each possible split point k.
            prefix_primes = set() # Primes in prefix part nums[0..k-1]
            suffix_primes = set(nums) & primes_set # Primes in suffix nums[k..] initially includes all nums elements. 
            
            for k in range(1, n): # Iterate over possible split points k (1 <= k < n) 
                prefix_primes.add(nums[k-1]) # Add element at k-1 to prefix set if it is a prime. 
                suffix_primes.discard(nums[k-1]) # Remove from suffix set as it moves into prefix. 
                max_distinct_primes = max(max_distinct_primes, len(prefix_primes & primes_set) + len(suffix_primes & primes_set)) 
                
            results.append(max_distinct_primes) # Store result after processing each query. 
        return results # Return results list with maximum distinct prime counts after each query update. 
# @lc code=end