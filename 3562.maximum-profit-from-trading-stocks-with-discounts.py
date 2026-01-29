#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)

        def dfs(u):
            # dp0[b]: max profit in subtree u if u's boss didn't buy
            # dp1[b]: max profit in subtree u if u's boss bought
            
            # Initial state: no children processed yet
            # We need to track the sum of children's dp0 and dp1 results
            # using knapsack merging.
            combined_dp0 = [0] * (budget + 1)
            combined_dp1 = [0] * (budget + 1)
            
            for v in adj[u]:
                v_dp0, v_dp1 = dfs(v)
                new_combined_dp0 = [0] * (budget + 1)
                new_combined_dp1 = [0] * (budget + 1)
                
                # Standard knapsack merge for children
                for b in range(budget + 1):
                    if combined_dp0[b] == 0 and combined_dp1[b] == 0 and b > 0:
                        # Optimization: skip empty budget levels if possible
                        pass 
                    for v_b in range(budget - b + 1):
                        if combined_dp0[b] + v_dp0[v_b] > new_combined_dp0[b + v_b]:
                            new_combined_dp0[b + v_b] = combined_dp0[b] + v_dp0[v_b]
                        if combined_dp1[b] + v_dp1[v_b] > new_combined_dp1[b + v_b]:
                            new_combined_dp1[b + v_b] = combined_dp1[b] + v_dp1[v_b]
                combined_dp0 = new_combined_dp0
                combined_dp1 = new_combined_dp1

            res_dp0 = [0] * (budget + 1)
            res_dp1 = [0] * (budget + 1)
            
            cost_full = present[u-1]
            profit_full = future[u-1] - cost_full
            cost_half = present[u-1] // 2
            profit_half = future[u-1] - cost_half

            for b in range(budget + 1):
                # Option 1: u does not buy. Children get no discount.
                res_dp0[b] = combined_dp0[b]
                res_dp1[b] = combined_dp0[b]
                
                # Option 2: u buys at full price. Children get discount.
                # Only possible for res_dp0 (boss didn't buy) and res_dp1 (boss bought)
                if b >= cost_full:
                    val = combined_dp1[b - cost_full] + profit_full
                    if val > res_dp0[b]: res_dp0[b] = val
                    if val > res_dp1[b]: res_dp1[b] = val
                
                # Option 3: u buys at half price. Children get discount.
                # Only possible if boss bought (res_dp1)
                if b >= cost_half:
                    val = combined_dp1[b - cost_half] + profit_half
                    if val > res_dp1[b]: res_dp1[b] = val
            
            return res_dp0, res_dp1

        final_dp0, _ = dfs(1)
        return max(final_dp0)
# @lc code=end