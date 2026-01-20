#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[m][r] stores the number of substrings ending at the previous position
        # that have a remainder of r when divided by m.
        # m ranges from 1 to 9.
        # r ranges from 0 to m-1.
        
        # Initialize DP table
        # dp[m] is a list of size m initialized to 0
        dp = [ [0] * m for m in range(10) ]
        
        ans = 0
        
        for char in s:
            digit = int(char)
            
            # We need a temporary DP table for the current step to avoid using
            # updated values from the current digit for the same digit's calculation
            next_dp = [ [0] * m for m in range(10) ]
            
            for m in range(1, 10):
                # Update existing substrings remainders
                # The remainder r becomes (r * 10 + digit) % m
                for r in range(m):
                    if dp[m][r] > 0:
                        new_r = (r * 10 + digit) % m
                        next_dp[m][new_r] += dp[m][r]
                
                # Start a new substring consisting of just the current digit
                new_r = digit % m
                next_dp[m][new_r] += 1
            
            dp = next_dp
            
            # If the current digit is non-zero, add the count of substrings
            # ending here that are divisible by this digit (remainder 0 mod digit)
            if digit != 0:
                ans += dp[digit][0]
                
        return ans
# @lc code=end