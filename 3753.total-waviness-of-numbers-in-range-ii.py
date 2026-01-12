#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n):
            s = str(n)
            
            @lru_cache(None)
            def dp(idx, last1, last2, is_less, is_started):
                if idx == len(s):
                    return 0, 1 # (total waviness, count of numbers)
                
                res_waviness = 0
                res_count = 0
                limit = int(s[idx]) if not is_less else 9
                
                for d in range(limit + 1):
                    new_less = is_less or (d < limit)
                    new_started = is_started or (d > 0)
                    
                    # Calculate if last1 is a peak or valley
                    # last2, last1, d
                    waviness_inc = 0
                    if is_started and last2 != -1 and last1 != -1:
                        if last2 < last1 > d:
                            waviness_inc = 1
                        elif last2 > last1 < d:
                            waviness_inc = 1
                    
                    sub_waviness, sub_count = dp(idx + 1, d if new_started else -1, last1 if new_started else -1, new_less, new_started)
                    
                    res_waviness += sub_waviness + (waviness_inc * sub_count)
                    res_count += sub_count
                
                return res_waviness, res_count

            return dp(0, -1, -1, False, False)[0]

        return solve(num2) - solve(num1 - 1)
# @lc code=end