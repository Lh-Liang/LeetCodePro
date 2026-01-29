#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#
# @lc code=start
from typing import List
from math import gcd

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # Precompute log
        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i // 2] + 1
        # Sparse table
        LOG = 18  # sufficient for 1e5
        st = [[0] * LOG for _ in range(n)]
        for i in range(n):
            st[i][0] = nums[i]
        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                st[i][j] = gcd(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        
        def query(l: int, r: int) -> int:
            length = r - l + 1
            k = logs[length]
            return gcd(st[l][k], st[r - (1 << k) + 1][k])
        
        def can_achieve(K: int) -> bool:
            M = K + 1
            if M > n:
                return True
            bad = []
            for i in range(n - M + 1):
                if query(i, i + M - 1) >= 2:
                    bad.append((i, i + M - 1))
            if not bad:
                return True
            bad.sort(key=lambda x: x[1])
            i = 0
            changes = 0
            while i < len(bad):
                pos = bad[i][1]
                changes += 1
                while i < len(bad) and bad[i][0] <= pos:
                    i += 1
            return changes <= maxC
        
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if can_achieve(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

# @lc code=end