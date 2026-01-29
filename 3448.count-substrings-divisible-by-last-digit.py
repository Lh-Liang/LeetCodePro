#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[d][r] stores the number of substrings ending at the current index
        # that have a remainder r when divided by divisor d (1-9).
        dp = [[0] * 10 for _ in range(10)]
        total_count = 0
        
        for char in s:
            digit = int(char)
            # next_dp will store the counts for the next index
            next_dp = [[0] * 10 for _ in range(10)]
            
            # For each potential divisor d from 1 to 9
            for d in range(1, 10):
                # Update remainders for all substrings ending at the previous character
                for r in range(d):
                    if dp[d][r] > 0:
                        new_remainder = (r * 10 + digit) % d
                        next_dp[d][new_remainder] += dp[d][r]
                
                # Include the new substring starting and ending at the current character
                next_dp[d][digit % d] += 1
            
            # If the current digit is non-zero, it is a valid divisor.
            # Add all substrings ending here that are divisible by this digit.
            if digit > 0:
                total_count += next_dp[digit][0]
            
            dp = next_dp
            
        return total_count
# @lc code=end