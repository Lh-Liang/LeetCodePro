#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
from typing import List
import math

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)
            
        # 1-indexed conversion for convenience
        pres = [0] + present
        fut = [0] + future

        def dfs(u):
            # dp_bought[b]: max profit in subtree u if u's boss bought stock, with budget b
            # dp_not_bought[b]: max profit in subtree u if u's boss did not buy stock, with budget b
            dp_bought = [0] * (budget + 1)
            dp_not_bought = [0] * (budget + 1)
            
            # Scenario 1: u does not buy
            # Scenario 2: u buys at full price
            # Scenario 3: u buys at discount (only for dp_bought)
            
            # Initialize dp_not_bought with Scenario 1 & 2
            # u does not buy: cost 0, profit 0 (already 0s)
            # u buys full: cost pres[u], profit fut[u] - pres[u]
            full_cost = pres[u]
            full_profit = max(0, fut[u] - pres[u])
            
            # Initialize dp_bought with Scenario 1, 2 & 3
            # u buys discount: cost pres[u]//2, profit fut[u] - pres[u]//2
            disc_cost = pres[u] // 2
            disc_profit = max(0, fut[u] - disc_cost)
            
            # Temporary arrays to handle initial state before merging children
            base_not_bought = [0] * (budget + 1)
            if full_cost <= budget:
                for b in range(full_cost, budget + 1):
                    base_not_bought[b] = full_profit
            
            base_bought = [0] * (budget + 1)
            if full_cost <= budget:
                for b in range(full_cost, budget + 1):
                    base_bought[b] = max(base_bought[b], full_profit)
            if disc_cost <= budget:
                for b in range(disc_cost, budget + 1):
                    base_bought[b] = max(base_bought[b], disc_profit)
            
            # We track whether u bought stock to decide child's discount
            # If u bought, child gets dp_bought. If u didn't, child gets dp_not_bought.
            
            # To handle this correctly, we need two states for the subtree merge:
            # f_bought[b]: max profit if u's boss bought, budget b
            # f_not_bought[b]: max profit if u's boss didn't buy, budget b
            
            # dp_u_buys[b]: max profit of children given u buys
            # dp_u_not_buys[b]: max profit of children given u doesn't buy
            dp_u_buys = [0] * (budget + 1)
            dp_u_not_buys = [0] * (budget + 1)
            
            for v in adj[u]:
                v_bought, v_not_bought = dfs(v)
                for b in range(budget, -1, -1):
                    for k in range(b + 1):
                        dp_u_buys[b] = max(dp_u_buys[b], dp_u_buys[b-k] + v_bought[k])
                        dp_u_not_buys[b] = max(dp_u_not_buys[b], dp_u_not_buys[b-k] + v_not_bought[k])
            
            # Combine base state of u with child results
            res_bought = [0] * (budget + 1)
            res_not_bought = [0] * (budget + 1)
            
            for b in range(budget + 1):
                # boss bought: u can buy discounted, full, or not at all
                # If u buys (full or discounted), children use dp_u_buys
                # If u doesn't buy, children use dp_u_not_buys
                
                # u doesn't buy
                res_bought[b] = max(res_bought[b], dp_u_not_buys[b])
                res_not_bought[b] = max(res_not_bought[b], dp_u_not_buys[b])
                
                # u buys discounted (only if boss bought)
                if b >= disc_cost:
                    res_bought[b] = max(res_bought[b], disc_profit + dp_u_buys[b - disc_cost])
                
                # u buys full
                if b >= full_cost:
                    res_bought[b] = max(res_bought[b], full_profit + dp_u_buys[b - full_cost])
                    res_not_bought[b] = max(res_not_bought[b], full_profit + dp_u_buys[b - full_cost])
            
            return res_bought, res_not_bought

        res_bought, res_not_bought = dfs(1)
        return res_not_bought[budget]
# @lc code=end