#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[k][rem] stores the count of substrings ending at current index
        # that have remainder 'rem' when divided by 'k'.
        dp = [[0] * 10 for _ in range(10)]
        total_count = 0
        
        for char in s:
            v = int(char)
            new_dp = [[0] * 10 for _ in range(10)]
            
            for k in range(1, 10):
                # Case: The substring is just the current digit itself
                new_dp[k][v % k] += 1
                
                # Case: Extend previous substrings
                for rem in range(k):
                    if dp[k][rem] > 0:
                        new_rem = (rem * 10 + v) % k
                        new_dp[k][new_rem] += dp[k][rem]
            
            # If the last digit is non-zero, add substrings divisible by it
            if v > 0:
                total_count += new_dp[v][0]
            
            dp = new_dp
            
        return total_count
# @lc code=end