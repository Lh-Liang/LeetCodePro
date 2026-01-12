#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[d][r] stores the number of substrings ending at the current index
        # that have a remainder 'r' when divided by 'd'.
        dp = [[0] * 10 for _ in range(10)]
        total_count = 0
        
        for char in s:
            v = ord(char) - 48
            # next_dp will store the counts for substrings ending at the current character
            next_dp = [[0] * 10 for _ in range(10)]
            
            for d in range(1, 10):
                # For each divisor d, update the remainders for existing substrings
                # extended by the current digit v.
                d_row = dp[d]
                nd_row = next_dp[d]
                for r in range(d):
                    if d_row[r] > 0:
                        new_rem = (r * 10 + v) % d
                        nd_row[new_rem] += d_row[r]
                
                # Also add the substring consisting of only the current digit itself.
                nd_row[v % d] += 1
            
            # If the current digit is non-zero, it can be a divisor.
            # Add the count of substrings ending here that are divisible by v.
            if v > 0:
                total_count += next_dp[v][0]
            
            dp = next_dp
            
        return total_count
# @lc code=end