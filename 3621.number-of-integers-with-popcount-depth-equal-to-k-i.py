#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        from functools import lru_cache
        
        # Memoization cache for popcount depths
        @lru_cache(None)
        def calculate_depth(x):
            depth = 0
            while x != 1:
                x = bin(x).count('1')
                depth += 1
            return depth
        
        count = 0
        
        # Implement efficient logic below using theoretical insights on popcounts.
        # Avoid arbitrary limits by ensuring scalable computation.
        for i in range(1, n + 1):
            if calculate_depth(i) == k:
                count += 1
        
        # Consider adding logic with dynamic programming or combinatorial methods if needed.
        return count
# @lc code=end