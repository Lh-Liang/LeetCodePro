#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
class Solution:
    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def get_distinct_primes(self, nums):
        prime_set = set()
        for num in nums:
            if self.is_prime(num):
                prime_set.add(num)
        return prime_set
    
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        results = []
        for idx, val in queries:
            nums[idx] = val # Update the array with the query value.
            max_distinct_primes = 0 # Initialize max distinct primes count.
            # Attempt splitting at every possible k value.
            for k in range(1, len(nums)):
                prefix_primes = self.get_distinct_primes(nums[:k]) # Distinct primes in prefix.
                suffix_primes = self.get_distinct_primes(nums[k:]) # Distinct primes in suffix.
                current_count = len(prefix_primes) + len(suffix_primes) # Total distinct primes count.
                max_distinct_primes = max(max_distinct_primes, current_count) # Update max count if needed.
            results.append(max_distinct_primes) # Append result for current query.
        return results # Return all results for queries.
# @lc code=end