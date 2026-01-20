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
        
        # Helper to merge two DP arrays (knapsack convolution)
        # dp[i] = max profit with budget i
        def merge(dp1, dp2):
            new_dp = [-1] * (budget + 1)
            # Extract valid entries to avoid iterating over -1s
            items1 = [(c, p) for c, p in enumerate(dp1) if p != -1]
            items2 = [(c, p) for c, p in enumerate(dp2) if p != -1]
            
            for c1, p1 in items1:
                for c2, p2 in items2:
                    if c1 + c2 <= budget:
                        if p1 + p2 > new_dp[c1 + c2]:
                            new_dp[c1 + c2] = p1 + p2
            return new_dp

        def dfs(u):
            # agg_0: max profit from children assuming u DOES NOT buy
            # agg_1: max profit from children assuming u DOES buy
            
            # Base initialization: 0 cost, 0 profit
            agg_0 = [-1] * (budget + 1)
            agg_0[0] = 0
            agg_1 = [-1] * (budget + 1)
            agg_1[0] = 0
            
            # Merge results from children
            for v in adj[u]:
                v_res0, v_res1 = dfs(v)
                agg_0 = merge(agg_0, v_res0)
                agg_1 = merge(agg_1, v_res1)
            
            # Calculate results for current node u
            
            # Case 1: Parent of u did NOT buy (u pays full price)
            # Option A: u doesn't buy. We use agg_0 (children see u not buying).
            res0 = list(agg_0)
            
            # Option B: u buys. We use agg_1 (children see u buying).
            # u pays full price.
            cost_full = present[u]
            profit_full = future[u] - cost_full
            
            if cost_full <= budget:
                for c, p in enumerate(agg_1):
                    if p != -1 and c + cost_full <= budget:
                        if p + profit_full > res0[c + cost_full]:
                            res0[c + cost_full] = p + profit_full
            
            # Case 2: Parent of u DID buy (u pays half price)
            # Option A: u doesn't buy. We use agg_0.
            res1 = list(agg_0)
            
            # Option B: u buys. We use agg_1.
            # u pays discounted price.
            cost_half = present[u] // 2
            profit_half = future[u] - cost_half
            
            if cost_half <= budget:
                for c, p in enumerate(agg_1):
                    if p != -1 and c + cost_half <= budget:
                        if p + profit_half > res1[c + cost_half]:
                            res1[c + cost_half] = p + profit_half
                            
            return res0, res1

        # Root is employee 1 (index 0). CEO has no boss, so effectively boss didn't buy.
        final_res0, _ = dfs(0)
        return max(final_res0)
# @lc code=end