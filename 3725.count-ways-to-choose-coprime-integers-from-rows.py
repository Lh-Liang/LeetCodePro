#
# @lc app=leetcode id=3725 lang=python3
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

from typing import List
from math import gcd
from functools import lru_cache

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(mat), len(mat[0])
        
        @lru_cache(None)
        def dfs(row: int, current_gcd: int) -> int:
            if row == m:  # If we've processed all rows
                return 1 if current_gcd == 1 else 0
            
            count = 0
            # Try each number in the current row
            for num in mat[row]:
                new_gcd = gcd(current_gcd, num)
                # Only continue if there's still a chance to reach gcd of 1
                if new_gcd <= current_gcd:
                    count += dfs(row + 1, new_gcd)
                    count %= MOD
            return count
        
        total_ways = dfs(0, 0)
        return total_ways % MOD