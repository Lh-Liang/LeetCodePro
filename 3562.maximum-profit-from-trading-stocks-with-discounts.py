#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u-1].append(v-1)
        
        # Helper to merge two DP arrays: dp[cost] = profit
        # Performs convolution: new_dp[i+j] = max(new_dp[i+j], dp1[i] + dp2[j])
        def merge(dp1, dp2):
            new_dp = [-float('inf')] * (budget + 1)
            # Iterate over valid costs in dp1
            for i in range(budget + 1):
                if dp1[i] == -float('inf'): continue
                v1 = dp1[i]
                # Iterate over valid costs in dp2 such that total cost <= budget
                for j in range(budget - i + 1):
                    if dp2[j] == -float('inf'): continue
                    s = v1 + dp2[j]
                    if s > new_dp[i+j]:
                        new_dp[i+j] = s
            return new_dp

        def dfs(u):
            # accum_buy: max profit from children subtrees given u buys (children get discount)
            # accum_nobuy: max profit from children subtrees given u doesn't buy (children pay full)
            
            # Base case: cost 0, profit 0
            accum_buy = [-float('inf')] * (budget + 1)
            accum_buy[0] = 0
            
            accum_nobuy = [-float('inf')] * (budget + 1)
            accum_nobuy[0] = 0
            
            for v in adj[u]:
                child_res_parent_bought, child_res_parent_not_bought = dfs(v)
                accum_buy = merge(accum_buy, child_res_parent_bought)
                accum_nobuy = merge(accum_nobuy, child_res_parent_not_bought)
            
            # Calculate the two result tables for u depending on u's parent's action
            
            res_parent_bought = [-float('inf')] * (budget + 1)
            res_parent_not_bought = [-float('inf')] * (budget + 1)
            
            # Precompute costs and profits for u
            cost_discount = present[u] // 2
            profit_discount = future[u] - cost_discount
            
            cost_full = present[u]
            profit_full = future[u] - cost_full
            
            # --- Construct res_parent_bought (Parent of u bought) ---
            # Option 1: u buys (gets discount). 
            # We use accum_buy because u buying triggers discount for children.
            if cost_discount <= budget:
                for c in range(budget - cost_discount + 1):
                    if accum_buy[c] > -float('inf'):
                        val = accum_buy[c] + profit_discount
                        if val > res_parent_bought[c + cost_discount]:
                            res_parent_bought[c + cost_discount] = val
                            
            # Option 2: u doesn't buy.
            # We use accum_nobuy because u not buying means no discount for children.
            for c in range(budget + 1):
                if accum_nobuy[c] > -float('inf'):
                    if accum_nobuy[c] > res_parent_bought[c]:
                        res_parent_bought[c] = accum_nobuy[c]

            # --- Construct res_parent_not_bought (Parent of u didn't buy) ---
            # Option 1: u buys (pays full price).
            # We use accum_buy because u buying triggers discount for children.
            if cost_full <= budget:
                for c in range(budget - cost_full + 1):
                    if accum_buy[c] > -float('inf'):
                        val = accum_buy[c] + profit_full
                        if val > res_parent_not_bought[c + cost_full]:
                            res_parent_not_bought[c + cost_full] = val
            
            # Option 2: u doesn't buy.
            # We use accum_nobuy.
            for c in range(budget + 1):
                if accum_nobuy[c] > -float('inf'):
                    if accum_nobuy[c] > res_parent_not_bought[c]:
                        res_parent_not_bought[c] = accum_nobuy[c]
                        
            return res_parent_bought, res_parent_not_bought

        # Employee 1 is root (index 0). Root has no parent, so we take the 'parent not bought' case.
        _, root_res = dfs(0)
        
        return max(0, max(root_res))
# @lc code=end