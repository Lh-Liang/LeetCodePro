#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#
# @lc code=start
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        from functools import lru_cache
        import sys
        sys.setrecursionlimit(10000)
        # Precompute popcount-depth for all possible popcounts
        MAX_BITS = 70  # more than needed since n <= 1e15
        popcount_depth = [0] * (MAX_BITS+1)
        def get_depth(x):
            if x == 1:
                return 0
            if popcount_depth[x] != 0:
                return popcount_depth[x]
            popcount_depth[x] = 1 + get_depth(bin(x).count('1'))
            return popcount_depth[x]
        for i in range(1, MAX_BITS+1):
            get_depth(i)
        # Count numbers <= n with exactly cnt ones
        def count(N, cnt):
            bits = list(map(int, bin(N)[2:]))
            L = len(bits)
            @lru_cache(None)
            def dp(pos, tight, ones):
                if ones < 0:
                    return 0
                if pos == L:
                    return 1 if ones == 0 else 0
                res = 0
                up = bits[pos] if tight else 1
                for d in range(up+1):
                    res += dp(pos+1, tight and d==up, ones-d)
                return res
            return dp(0, True, cnt)
        if k == 0:
            return 1 if n >= 1 else 0
        ans = 0
        for i in range(1, MAX_BITS+1):
            if popcount_depth[i] == k-1:
                ans += count(n, i)
        if k == 1:
            ans -= 1  # exclude number 1 (since its depth is 0)
        return ans
# @lc code=end