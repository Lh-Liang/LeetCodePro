#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        from functools import lru_cache
        import math
        # Precompute popcount-depth for all s in [1, 100]
        def popcount(x):
            return bin(x).count('1')
        depth = {0: -1, 1: 0}
        for s in range(2, 70):
            x = s
            d = 0
            while x != 1:
                x = popcount(x)
                d += 1
            depth[s] = d
        # For each s, count numbers <= n with exactly s set bits
        bits = list(map(int, bin(n)[2:]))
        L = len(bits)
        @lru_cache(None)
        def dp(pos, cnt, tight):
            if pos == L:
                return 1 if cnt == 0 else 0
            res = 0
            maxb = bits[pos] if tight else 1
            for b in range(maxb + 1):
                res += dp(pos + 1, cnt - b, tight and (b == maxb))
            return res
        ans = 0
        # Edge case: k == 0, only x=1 has popcount-depth 0
        if k == 0:
            if n >= 1:
                return 1
            else:
                return 0
        for s in range(1, L * 2):
            if depth.get(s, -1) == k - 1 and s > 0:
                cnt = dp(0, s, True)
                # Exclude 0
                if s == 1:
                    cnt -= 1
                ans += cnt
        return ans
# @lc code=end