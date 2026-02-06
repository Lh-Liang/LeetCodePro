#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def sieve_of_eratosthenes(max_num):
            is_prime = [True] * (max_num + 1)
            p = 2
            while (p * p <= max_num):
                if (is_prime[p] == True):
                    for i in range(p * p, max_num + 1, p):
                        is_prime[i] = False
                p += 1
            is_prime[0], is_prime[1] = False, False # 0 and 1 are not primes
            return {i for i in range(max_num + 1) if is_prime[i]}
        
        prime_set = sieve_of_eratosthenes(100000)
        result = []
        n = len(nums)
        
        def count_distinct_primes(arr):
            return len(set(filter(lambda x: x in prime_set, arr)))
        
        for idx, val in queries:
            nums[idx] = val # Update nums with the query value.
            left_primes_cumulative = [0] * n
            right_primes_cumulative = [0] * n
            left_distinct_primes = set()
            right_distinct_primes = set()
            
            # Calculate cumulative distinct primes from left to right
            for i in range(n):
                if nums[i] in prime_set:
                    left_distinct_primes.add(nums[i])
                left_primes_cumulative[i] = len(left_distinct_primes)
                
            # Calculate cumulative distinct primes from right to left
            for i in range(n-1, -1, -1):
                if nums[i] in prime_set:
                    right_distinct_primes.add(nums[i])
                right_primes_cumulative[i] = len(right_distinct_primes)
                
            # Calculate maximum distinct primes across any split point k
            max_distinct_primes = 0
            for k in range(1, n): # Try each possible split position k.
                max_distinct_primes = max(max_distinct_primes,
                                          left_primes_cumulative[k-1] + right_primes_cumulative[k])
                                          
            result.append(max_distinct_primes) # Store result for current query.
        
        return result # Return results of all queries. 
# @lc code=end