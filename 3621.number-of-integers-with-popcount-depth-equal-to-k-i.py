#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
import math

class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        
        # Precalculate popcount depths for [1, 64]
        # d(x) = 1 + d(popcount(x))
        depth = [0] * 65
        depth[1] = 0
        for i in range(2, 65):
            depth[i] = 1 + depth[bin(i).count('1')]
            
        def count_with_popcount(num, target_c):
            if target_c < 0:
                return 0
            s = bin(num)[2:]
            L = len(s)
            res = 0
            current_bits = 0
            for i in range(L):
                if s[i] == '1':
                    # If we set this bit to 0, we can choose the remaining bits freely
                    remaining_pos = L - 1 - i
                    needed = target_c - current_bits
                    if 0 <= needed <= remaining_pos:
                        res += math.comb(remaining_pos, needed)
                    current_bits += 1
            # Check the number n itself
            if current_bits == target_c:
                res += 1
            return res

        ans = 0
        # Iterate possible popcounts c for x in [1, n]
        # For x <= 10^15, max popcount is < 60
        for c in range(1, 61):
            if depth[c] == k - 1:
                ans += count_with_popcount(n, c)
        
        # Boundary case: k=1 requires d(popcount(x)) = 0, which means popcount(x) = 1.
        # count_with_popcount(n, 1) includes x=1 (2^0), but depth(1) is 0, not 1.
        if k == 1:
            ans -= 1
            
        return ans
# @lc code=end