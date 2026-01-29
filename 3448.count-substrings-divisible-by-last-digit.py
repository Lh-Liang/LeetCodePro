#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[d] is a list where dp[d][rem] is the number of substrings 
        # ending at the previous character that have remainder 'rem' when divided by 'd'.
        dp = [[0] * d for d in range(10)]
        ans = 0
        
        for char in s:
            v = int(char)
            next_dp = [[0] * d for d in range(10)]
            
            for d in range(1, 10):
                # Update existing substrings
                d_row = dp[d]
                nd_row = next_dp[d]
                for rem, count in enumerate(d_row):
                    if count > 0:
                        nd_row[(rem * 10 + v) % d] += count
                
                # Start a new substring at the current digit
                nd_row[v % d] += 1
            
            # If the current digit is the divisor, count substrings ending here with rem 0
            if v > 0:
                ans += next_dp[v][0]
            
            dp = next_dp
            
        return ans
# @lc code=end