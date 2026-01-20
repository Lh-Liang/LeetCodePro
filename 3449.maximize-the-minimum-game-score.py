#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#
# @lc code=start
from typing import List
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def possible(k: int) -> bool:
            n = len(points)
            need = [(k + points[i] - 1) // points[i] for i in range(n)]
            if sum(need) > m:
                return False
            suf = [0] * n
            suf[n - 1] = need[n - 1]
            for j in range(n - 2, -1, -1):
                suf[j] = max(need[j], suf[j + 1])
            base_r = [suf[i + 1] for i in range(n - 1)]
            # compute max_e for case 2
            max_e = n - 1
            for ii in range(1, n - 1):
                if base_r[ii] == 0:
                    max_e = ii
                    break
            sum_tail = sum(base_r[1:]) if n >= 3 else 0
            # case 1: e = 0
            r0_1 = max(base_r[0], max(0, need[0] - 1))
            sum_r1 = r0_1 + sum_tail
            total1 = 1 + 2 * sum_r1
            # case 2: max e >=1
            r0_2 = max(base_r[0], need[0])
            sum_r2 = r0_2 + sum_tail
            total2 = 1 + 2 * sum_r2 - max_e
            min_total = min(total1, total2)
            return min_total <= m
        
        low, high = 0, 10**18
        while low < high:
            mid = (low + high + 1) // 2
            if possible(mid):
                low = mid
            else:
                high = mid - 1
        return low
# @lc code=end