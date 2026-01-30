#
# @lc app=leetcode id=3470 lang=python3
#
# [3470] Permutations IV
#

# @lc code=start
from math import factorial
from itertools import islice

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        # Helper function to calculate number of valid alternating permutations for size m
        def count_alternating_permutations(m):
            if m <= 1:
                return 1
            dp = [0] * (m + 1)
            dp[0], dp[1] = 1, 1
            for i in range(2, m + 1):
                dp[i] = (i - 1) * (dp[i - 2] + dp[i - 1])
            return dp[m]
        
        if k > count_alternating_permutations(n):
            return []
        
        numbers = list(range(1, n+1))
        permutation = []
        remaining_k = k - 1 # Zero-indexed kth permutation
        odd, even = numbers[::2], numbers[1::2]
        
        for i in range(n):
            if i % 2 == 0: # Even index, choose from odd numbers (1-based)
                block_size = count_alternating_permutations(n - i - 1)
                index = remaining_k // block_size
                remaining_k %= block_size
                permutation.append(odd.pop(index))
            else: # Odd index, choose from even numbers (1-based)
                block_size = count_alternating_permutations(n - i - 1)
                index = remaining_k // block_size
                remaining_k %= block_size
                permutation.append(even.pop(index))
        
        return permutation
# @lc code=end