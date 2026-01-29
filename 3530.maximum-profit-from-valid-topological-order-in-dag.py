#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        pred_mask = [0] * n
        for u, v in edges:
            pred_mask[v] |= (1 << u)
        N = 1 << n
        NEG_INF = -10**18
        dp = [NEG_INF] * N
        dp[0] = 0
        pop = [0] * N
        for i in range(N):
            pop[i] = pop[i // 2] + (i & 1)
        for mask in range(1, N):
            pos = pop[mask]
            for v in range(n):
                if mask & (1 << v):
                    prev = mask ^ (1 << v)
                    if (pred_mask[v] & prev) == pred_mask[v]:
                        dp[mask] = max(dp[mask], dp[prev] + score[v] * pos)
        return dp[N - 1]
# @lc code=end