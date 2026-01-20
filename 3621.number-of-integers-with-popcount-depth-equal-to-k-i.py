#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        
        # Precompute depths for small m
        depths = [0] * 65
        for m in range(1, 65):
            y = m
            d = 0
            while y > 1:
                y = bin(y).count('1')
                d += 1
            depths[m] = d
        
        T = [m for m in range(1, 65) if depths[m] == k - 1]
        if not T:
            return 0
        
        # Binary representation of n, MSB first
        bits = []
        tmp = n
        while tmp:
            bits.append(tmp % 2)
            tmp //= 2
        bits = bits[::-1]
        L = len(bits)
        
        def count_for_target(target):
            memo = {}
            def dfs(pos, cursum, tight):
                if pos == L:
                    return 1 if cursum == target else 0
                key = (pos, cursum, tight)
                if key in memo:
                    return memo[key]
                res = 0
                upper = bits[pos] if tight else 1
                for d in range(2):
                    if d > upper:
                        continue
                    new_sum = cursum + d
                    if new_sum > target:
                        continue
                    new_tight = 1 if tight and d == upper else 0
                    res += dfs(pos + 1, new_sum, new_tight)
                memo[key] = res
                return res
            return dfs(0, 0, 1)
        
        ans = 0
        for t in T:
            ans += count_for_target(t)
        
        if k == 1:
            ans -= 1
        
        return ans
# @lc code=end