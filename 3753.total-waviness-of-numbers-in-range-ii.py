#
# @lc app=leetcode id=3753 lang=python3
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def total_upto(N: int) -> int:
            if N <= 0:
                return 0
            digits = list(map(int, str(N)))
            m = len(digits)

            @lru_cache(None)
            def dfs(pos: int, tight: int, started: int, last2: int, last1: int):
                # returns (count_numbers, sum_waviness) for all completions
                if pos == m:
                    return 1, 0

                limit = digits[pos] if tight else 9
                total_cnt = 0
                total_sum = 0

                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0

                    if not started:
                        if d == 0:
                            cnt, sm = dfs(pos + 1, ntight, 0, -1, -1)
                            total_cnt += cnt
                            total_sum += sm
                        else:
                            cnt, sm = dfs(pos + 1, ntight, 1, -1, d)
                            total_cnt += cnt
                            total_sum += sm
                    else:
                        inc = 0
                        if last2 != -1:
                            if (last1 > last2 and last1 > d) or (last1 < last2 and last1 < d):
                                inc = 1
                        cnt, sm = dfs(pos + 1, ntight, 1, last1, d)
                        total_cnt += cnt
                        total_sum += sm + inc * cnt

                return total_cnt, total_sum

            return dfs(0, 1, 0, -1, -1)[1]

        return total_upto(num2) - total_upto(num1 - 1)
# @lc code=end
