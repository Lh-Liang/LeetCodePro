#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n):
            if n < 100:
                return 0
            s = str(n)
            L = len(s)
            memo = {}

            def dp(pos, is_less, is_started, prev, pprev):
                state = (pos, is_less, is_started, prev, pprev)
                if state in memo:
                    return memo[state]
                
                if pos == L:
                    # Return (count=1, sum=0)
                    return 1, 0
                
                res_count = 0
                res_sum = 0
                limit = int(s[pos]) if not is_less else 9
                
                for d in range(limit + 1):
                    new_is_less = is_less or (d < limit)
                    if not is_started:
                        if d == 0:
                            # Still leading zero
                            c, s_val = dp(pos + 1, new_is_less, False, -1, -1)
                        else:
                            # First non-zero digit
                            c, s_val = dp(pos + 1, new_is_less, True, d, -1)
                        res_count += c
                        res_sum += s_val
                    else:
                        # is_started is True
                        inc = 0
                        # Evaluate if 'prev' is a peak or valley using 'pprev' and current 'd'
                        if pprev != -1:
                            if (pprev < prev > d) or (pprev > prev < d):
                                inc = 1
                        
                        c, s_val = dp(pos + 1, new_is_less, True, d, prev)
                        res_count += c
                        # Add the waviness contribution of 'prev' to the total sum
                        res_sum += s_val + inc * c
                
                memo[state] = (res_count, res_sum)
                return res_count, res_sum

            return dp(0, False, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)
# @lc code=end