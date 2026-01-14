#
# @lc app=leetcode id=3569 lang=python3
#
# [3569] Maximize Count of Distinct Primes After Split
#
# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Sieve of Eratosthenes to precompute primes
        MAX_NUM = 100001
        is_prime = [True] * MAX_NUM
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX_NUM**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, MAX_NUM, i):
                    is_prime[j] = False
        
        n = len(nums)
        result = []
        
        for idx, val in queries:
            # Update the array
            nums[idx] = val
            
            # Build prefix prime counts
            prefix_primes = []
            curr_set = set()
            for i in range(n):
                if is_prime[nums[i]]:
                    curr_set.add(nums[i])
                prefix_primes.append(len(curr_set))
            
            # Build suffix prime counts
            suffix_primes = [0] * n
            curr_set = set()
            for i in range(n - 1, -1, -1):
                if is_prime[nums[i]]:
                    curr_set.add(nums[i])
                suffix_primes[i] = len(curr_set)
            
            # Find the maximum sum for all possible splits
            max_count = 0
            for k in range(1, n):
                count = prefix_primes[k-1] + suffix_primes[k]
                max_count = max(max_count, count)
            
            result.append(max_count)
        
        return result
# @lc code=end