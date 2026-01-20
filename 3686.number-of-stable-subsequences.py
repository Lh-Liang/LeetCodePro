#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0:
            return 0
        p = [x % 2 for x in nums]
        prev = [[0] * 2 for _ in range(3)]
        for i in range(n):
            q = p[i]
            curr = [[0] * 2 for _ in range(3)]
            # Copy from prev
            for c in range(1, 3):
                for par in range(2):
                    curr[c][par] = prev[c][par]
            # Add single
            curr[1][q] = (curr[1][q] + 1) % MOD
            # Append to previous subsequences
            for prev_c in range(1, 3):
                for prev_par in range(2):
                    ways = prev[prev_c][prev_par]
                    if ways == 0:
                        continue
                    if q != prev_par:
                        curr[1][q] = (curr[1][q] + ways) % MOD
                    else:
                        new_c = prev_c + 1
                        if new_c <= 2:
                            curr[new_c][q] = (curr[new_c][q] + ways) % MOD
            prev = curr
        # Sum all
        total = 0
        for c in range(1, 3):
            for par in range(2):
                total = (total + prev[c][par]) % MOD
        return total

# @lc code=end