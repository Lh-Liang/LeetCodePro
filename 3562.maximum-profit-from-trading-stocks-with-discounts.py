#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)
        
        # Adjust arrays to 0-indexed
        present = [0] + present
        future = [0] + future

        memo = {}

        def solve(u, b, boss_bought):
            state = (u, b, boss_bought)
            if state in memo:
                return memo[state]
            
            # Option 1: u does not buy
            # dp[w] stores max profit for children using budget w
            dp_no_buy = [0] * (b + 1)
            for v in adj[u]:
                v_res = solve(v, b, False)
                for w in range(b, -1, -1):
                    for cost_v in range(w + 1):
                        dp_no_buy[w] = max(dp_no_buy[w], dp_no_buy[w - cost_v] + v_res[cost_v])
            
            # Option 2: u buys
            cost_u = (present[u] // 2) if boss_bought else present[u]
            profit_u = future[u] - cost_u
            
            dp_buy = [-float('inf')] * (b + 1)
            if cost_u <= b:
                temp_dp = [0] * (b - cost_u + 1)
                for v in adj[u]:
                    v_res = solve(v, b - cost_u, True)
                    for w in range(b - cost_u, -1, -1):
                        for cost_v in range(w + 1):
                            temp_dp[w] = max(temp_dp[w], temp_dp[w - cost_v] + v_res[cost_v])
                
                for w in range(cost_u, b + 1):
                    dp_buy[w] = profit_u + temp_dp[w - cost_u]
            
            res = [max(dp_no_buy[w], dp_buy[w]) for w in range(b + 1)]
            memo[state] = res
            return res

        final_dp = solve(1, budget, False)
        return max(0, max(final_dp))

# @lc code=end