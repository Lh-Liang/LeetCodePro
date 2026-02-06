# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#
# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0, 0], [0, 0]] # dp[even/odd][last parity] = count of subsequences ending with these properties
        total_stable = 0 # Total count of stable subsequences found so far
        for num in nums:
            parity = num % 2 # Determine parity of current number (even or odd)
            new_dp = [[0, 0], [0, 0]] # Temporary dp table for current number
            # Update dp counts based on current number's parity:
            # If current number is odd (1), increase sequences ending with odd numbers or continue even sequences followed by an odd number
            new_dp[parity][parity] = (dp[1-parity][parity] + 1) % MOD # New sequence from current or extend previous valid one by adding this number, starting new sequence as well.
            new_dp[parity][1-parity] = dp[parity][1-parity]
            # If current number is even (0), increase sequences ending with even numbers or continue odd sequences followed by an even number
            new_dp[1-parity][parity] = (dp[parity][1-parity] + dp[1-parity][1-parity]) % MOD 
            new_dp[1-parity][1-parity] = dp[1-parity][parity]
            # Update main dp table to new values for this iteration:
dp = new_dp 
total_stable += sum(sum(row) for row in dp) % MOD # Sum up all valid subsequences found so far 
total_stable %= MOD 
return total_stable % MOD # Return result modulo as required "# @lc code=end