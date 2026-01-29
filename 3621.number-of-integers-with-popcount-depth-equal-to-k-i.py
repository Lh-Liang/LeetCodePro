#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        def popcount(x: int) -> int:
            cnt = 0
            while x:
                cnt += x & 1
                x >>= 1
            return cnt
        
        def pop_depth(x: int) -> int:
            d = 0
            while x != 1:
                x = popcount(x)
                d += 1
            return d
        
        if k == 0:
            return 1 if n >= 1 else 0
        
        good_s = [s for s in range(1, 65) if pop_depth(s) == k - 1]
        
        def count_ones(target: int) -> int:
            if target == 0 or n == 0:
                return 0
            bits = []
            tmp = n
            while tmp > 0:
                bits.append(tmp % 2)
                tmp //= 2
            bits = bits[::-1]  # MSB first
            L = len(bits)
            memo = {}
            
            def dp(pos: int, tight: int, cnt: int) -> int:
                if pos == L:
                    return cnt == target
                key = (pos, tight, cnt)
                if key in memo:
                    return memo[key]
                ans = 0
                upper = bits[pos] if tight else 1
                for d in range(2):
                    if d > upper:
                        continue
                    new_tight = 1 if tight and d == upper else 0
                    new_cnt = cnt + d
                    if new_cnt > target:
                        continue
                    ans += dp(pos + 1, new_tight, new_cnt)
                memo[key] = ans
                return ans
            return dp(0, 1, 0)
        
        ans = sum(count_ones(s) for s in good_s)
        if k == 1:
            ans -= 1
        return ans

# @lc code=end