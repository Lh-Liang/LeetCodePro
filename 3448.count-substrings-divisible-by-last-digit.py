#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        # dp[d][r] stores the number of substrings ending at the current index
        # that have a remainder r when divided by d.
        dp = [[0] * d for d in range(10)]
        
        for char in s:
            v = int(char)
            # Create a new DP table for the next position
            new_dp = [[0] * d for d in range(10)]
            
            for d in range(1, 10):
                # For each possible divisor d, update the counts of remainders
                # based on adding the current digit v to the end of previous substrings.
                curr_d_dp = dp[d]
                curr_new_d_dp = new_dp[d]
                
                for r in range(d):
                    count = curr_d_dp[r]
                    if count > 0:
                        new_rem = (r * 10 + v) % d
                        curr_new_d_dp[new_rem] += count
                
                # Account for the single-digit substring ending at the current position
                curr_new_d_dp[v % d] += 1
            
            # If the current digit is non-zero, it acts as a divisor for all
            # substrings ending at this position.
            if v > 0:
                ans += new_dp[v][0]
            
            dp = new_dp
            
        return ans
# @lc code=end