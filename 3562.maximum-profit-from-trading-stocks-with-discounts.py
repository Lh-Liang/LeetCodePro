#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

from typing import List
import sys

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        sys.setrecursionlimit(10**7)
        B = budget
        INF = 10**18

        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        def merge(a: List[int], b: List[int]) -> List[int]:
            """Knapsack convolution: both arrays are length B+1, -INF means unreachable."""
            res = [-INF] * (B + 1)
            for i in range(B + 1):
                if a[i] <= -INF // 2:
                    continue
                maxj = B - i
                for j in range(maxj + 1):
                    if b[j] <= -INF // 2:
                        continue
                    val = a[i] + b[j]
                    if val > res[i + j]:
                        res[i + j] = val
            return res

        def dfs(u: int):
            # compute dp for children first
            child_dps = [dfs(v) for v in children[u]]  # list of (dp0, dp1)

            # Option A: do not buy u (independent of parent state)
            notBuy = [-INF] * (B + 1)
            notBuy[0] = 0
            for dp0c, dp1c in child_dps:
                notBuy = merge(notBuy, dp0c)  # children see parent not bought

            # Option B: buy u (depends on parent state)
            cost0 = present[u]
            cost1 = present[u] // 2
            prof0 = future[u] - cost0
            prof1 = future[u] - cost1

            buy0 = [-INF] * (B + 1)
            if cost0 <= B:
                buy0[cost0] = prof0
            for dp0c, dp1c in child_dps:
                buy0 = merge(buy0, dp1c)  # children see parent bought

            buy1 = [-INF] * (B + 1)
            if cost1 <= B:
                buy1[cost1] = prof1
            for dp0c, dp1c in child_dps:
                buy1 = merge(buy1, dp1c)

            dp0 = [max(notBuy[c], buy0[c]) for c in range(B + 1)]
            dp1 = [max(notBuy[c], buy1[c]) for c in range(B + 1)]
            return dp0, dp1

        dp0_root, _ = dfs(0)
        return max(0, max(dp0_root))
# @lc code=end
