#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        result = 0
        # dp[i][0] tracks stable sequences ending at i with last element even
        # dp[i][1] tracks stable sequences ending at i with last element odd
        dp = [[0, 0] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            num_parity = nums[i - 1] % 2
            # Add the number itself as a new subsequence
            dp[i][num_parity] = (dp[i][num_parity] + 1) % MOD
            
            # Extend previous stable sequences ending with different parity
            if i > 1:
                dp[i][num_parity] = (dp[i][num_parity] + dp[i - 1][1 - num_parity]) % MOD
                
            # Extend previous stable sequences ending with same parity but not forming an invalid streak of three
            if i > 2 and nums[i - 2] % 2 == num_parity and nums[i - 3] % 2 == num_parity:
                continue # Skip adding this to avoid invalid streaks of three consecutive same parity numbers.
            elif i > 1:
                dp[i][num_parity] = (dp[i][num_parity] + dp[i - 1][num_parity]) % MOD
                
            # Accumulate total stable subsequences ending at this point
            result = (result + dp[i][num_parity]) % MOD
        return result # @lc code=end