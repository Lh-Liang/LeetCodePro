#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

import math
from typing import List

# @lc code=start
class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Build sparse table for GCD
        LOG = 18  # 2^17 > 1e5
        st = [[0] * LOG for _ in range(n)]
        for i in range(n):
            st[i][0] = nums[i]
        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                st[i][j] = math.gcd(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        
        def query(L: int, R: int) -> int:
            length = R - L + 1
            k = (length).bit_length() - 1
            return math.gcd(st[L][k], st[R - (1 << k) + 1][k])
        
        def min_hits(L: int) -> int:
            if L > n:
                return 0
            bad_starts = []
            for i in range(n - L + 1):
                if query(i, i + L - 1) >= 2:
                    bad_starts.append(i)
            if not bad_starts:
                return 0
            count = 0
            i = 0
            m = len(bad_starts)
            while i < m:
                si = bad_starts[i]
                p = si + L - 1
                count += 1
                while i < m and bad_starts[i] <= p:
                    i += 1
            return count
        
        def can_achieve(K: int) -> bool:
            L = K + 1
            return min_hits(L) <= maxC
        
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if can_achieve(mid):
                high = mid
            else:
                low = mid + 1
        return low

# @lc code=end