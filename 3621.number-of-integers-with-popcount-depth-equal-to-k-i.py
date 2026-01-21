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
        
        # Precompute depth for values 1 to 64
        depths = [0] * 65
        depths[1] = 0
        for i in range(2, 65):
            pop = bin(i).count('1')
            depths[i] = 1 + depths[pop]
            
        # Find all target popcounts c such that depth(c) == k-1
        targets = []
        for c in range(1, 65):
            if depths[c] == k - 1:
                targets.append(c)
        
        if not targets:
            return 0
            
        def countWithPopcount(limit, target_c):
            if target_c < 0:
                return 0
            s = bin(limit)[2:]
            L = len(s)
            res = 0
            current_c = 0
            for i in range(L):
                if s[i] == '1':
                    # If we pick '0' at this position
                    remaining_positions = L - 1 - i
                    needed_c = target_c - current_c
                    if 0 <= needed_c <= remaining_positions:
                        res += math.comb(remaining_positions, needed_c)
                    current_c += 1
            if current_c == target_c:
                res += 1
            return res

        total_count = 0
        for c in targets:
            total_count += countWithPopcount(n, c)
            
        # Special case: if k=1, targets includes c=1. 
        # countWithPopcount(n, 1) includes x=1, but d(1)=0, not 1.
        if k == 1:
            total_count -= 1
            
        return total_count
# @lc code=end