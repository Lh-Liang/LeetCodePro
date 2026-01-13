#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

from typing import List
from array import array

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        pre = [0] * n
        for u, v in edges:
            pre[v] |= 1 << u

        N = 1 << n
        dp = array('q', [-1]) * N
        dp[0] = 0

        for mask in range(N):
            base = dp[mask]
            if base < 0:
                continue
            k = mask.bit_count()  # already placed nodes
            pos = k + 1

            # try placing any available node next
            for v in range(n):
                bit = 1 << v
                if mask & bit:
                    continue
                if (pre[v] & mask) != pre[v]:
                    continue
                nm = mask | bit
                val = base + score[v] * pos
                if val > dp[nm]:
                    dp[nm] = val

        return dp[N - 1]
# @lc code=end
