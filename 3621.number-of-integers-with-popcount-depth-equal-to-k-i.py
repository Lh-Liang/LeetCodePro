#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        def popcount(x):
            return bin(x).count('1')
        
        def depth(x):
            d = 0
            while x != 1:
                x = popcount(x)
                d += 1
            return d
        
        count = 0
        for i in range(1, n + 1):
            if depth(i) == k:
                count += 1
        return count
# @lc code=end