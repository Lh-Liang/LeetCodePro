#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # Precompute dependency masks for each node
        dep = [0] * n
        for u, v in edges:
            dep[v] |= 1 << u

        # dp[mask]: max profit using nodes in mask
        dp = [None] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] is None:
                continue
            num_placed = bin(mask).count('1')
            for i in range(n):
                if not (mask & (1 << i)) and (dep[i] & mask) == dep[i]:
                    # Node i can be placed next
                    next_mask = mask | (1 << i)
                    profit = dp[mask] + score[i] * (num_placed + 1)
                    if dp[next_mask] is None or profit > dp[next_mask]:
                        dp[next_mask] = profit
        return dp[(1 << n) - 1]
# @lc code=end