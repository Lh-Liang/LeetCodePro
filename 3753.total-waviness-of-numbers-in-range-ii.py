#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#
# @lc code=start
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def dp_solve(max_str):
            target_len = len(max_str)
            if target_len < 3:
                return 0
            
            memo = {}
            
            def dp(pos, tight, prev, prev_prev):
                if pos == target_len:
                    return (1, 0)
                
                state = (pos, tight, prev, prev_prev)
                if state in memo:
                    return memo[state]
                
                limit = int(max_str[pos]) if tight else 9
                start = 1 if pos == 0 else 0
                
                total_count = 0
                total_waviness = 0
                
                for digit in range(start, limit + 1):
                    new_tight = tight and (digit == limit)
                    
                    wave_contrib = 0
                    if 2 <= pos <= target_len - 1 and prev != -1 and prev_prev != -1:
                        if prev > prev_prev and prev > digit:
                            wave_contrib = 1
                        elif prev < prev_prev and prev < digit:
                            wave_contrib = 1
                    
                    sub_count, sub_waviness = dp(pos + 1, new_tight, digit, prev)
                    
                    total_count += sub_count
                    total_waviness += sub_waviness + wave_contrib * sub_count
                
                memo[state] = (total_count, total_waviness)
                return (total_count, total_waviness)
            
            _, waviness = dp(0, True, -1, -1)
            return waviness
        
        def solve(n):
            if n < 100:
                return 0
            
            total = 0
            n_str = str(n)
            n_len = len(n_str)
            
            for length in range(3, n_len):
                max_val = 10 ** length - 1
                total += dp_solve(str(max_val))
            
            if n_len >= 3:
                total += dp_solve(n_str)
            
            return total
        
        return solve(num2) - solve(num1 - 1)
# @lc code=end