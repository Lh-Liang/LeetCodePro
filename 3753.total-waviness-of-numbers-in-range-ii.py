#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(s):
            digits = list(map(int, str(s)))
            n = len(digits)
            # memo key: (index, second_last_digit, last_digit, is_less, is_started)
            # value: (count_of_numbers, sum_of_waviness)
            memo = {}

            def dp(idx, second_last, last, is_less, is_started):
                if idx == n:
                    return 1, 0
                
                state = (idx, second_last, last, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = digits[idx] if not is_less else 9
                total_count = 0
                total_waviness = 0
                
                for d in range(limit + 1):
                    new_less = is_less or (d < limit)
                    new_started = is_started or (d > 0)
                    
                    if not new_started:
                        # Still in leading zeros
                        c, w = dp(idx + 1, 10, 10, new_less, False)
                        total_count += c
                        total_waviness += w
                    else:
                        # Check if the previous digit (last) becomes a peak or valley
                        # This requires a valid 3-digit window: second_last, last, d
                        current_contribution = 0
                        if second_last != 10 and last != 10:
                            if (last > second_last and last > d) or (last < second_last and last < d):
                                current_contribution = 1
                        
                        # Determine args for next call
                        # If this is the very first digit (is_started was False), 
                        # then effectively second_last remains "empty" (10) for the next state,
                        # and last becomes d.
                        # If we had already started, we shift the window.
                        next_second_last = 10 if not is_started else last
                        next_last = d
                        
                        c, w = dp(idx + 1, next_second_last, next_last, new_less, True)
                        
                        total_count += c
                        total_waviness += w + (c * current_contribution)
                
                memo[state] = (total_count, total_waviness)
                return total_count, total_waviness

            return dp(0, 10, 10, False, False)[1]

        return solve(num2) - solve(num1 - 1)
# @lc code=end