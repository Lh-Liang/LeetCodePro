#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        from collections import defaultdict
        # Precompute dependency bitmask for each node
        dep = [0] * n
        for u, v in edges:
            dep[v] |= 1 << u

        size = 1 << n
        dp = [-1] * size
        dp[0] = 0
        for mask in range(size):
            k = bin(mask).count('1')  # current position (0-based), so position = k+1
            for i in range(n):
                if not (mask & (1 << i)) and (dep[i] & mask) == dep[i]:
                    nxt = mask | (1 << i)
                    profit = dp[mask] + score[i] * (k + 1)
                    if dp[nxt] < profit:
                        dp[nxt] = profit
        return dp[size-1]
# @lc code=end