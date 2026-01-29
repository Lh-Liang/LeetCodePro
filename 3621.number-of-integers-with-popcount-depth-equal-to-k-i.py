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
        
        def calculate_popcount_depth(x):
            depth = 0
            while x != 1:
                x = popcount(x)
                depth += 1
            return depth
        
        # Optimization step using memorization or bit manipulation methodologies could be added here.
        # Store precomputed depths if needed, not necessary for small constraints but crucial for large n.
        count = 0
        for i in range(1, n + 1):
            if calculate_popcount_depth(i) == k:
                count += 1
        return count
# @lc code=end