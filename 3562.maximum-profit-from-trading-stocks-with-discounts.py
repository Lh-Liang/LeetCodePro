#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)

        def dfs(u):
            # dp0[c]: max profit in subtree u if u's boss didn't buy, using budget c
            # dp1[c]: max profit in subtree u if u's boss did buy, using budget c
            # Initialize with -infinity to represent unreachable states
            dp0 = [-float('inf')] * (budget + 1)
            dp1 = [-float('inf')] * (budget + 1)
            
            # Base case: node u decisions
            # Case 1: u doesn't buy. Cost 0. Children use dp[v][0]
            u_not_buy = [0] * (budget + 1)
            
            # Case 2: u buys at full price. Cost present[u-1]. Children use dp[v][1]
            u_buy_full = [-float('inf')] * (budget + 1)
            cost_full = present[u - 1]
            if cost_full <= budget:
                u_buy_full[cost_full] = future[u - 1] - cost_full
                
            # Case 3: u buys at discount. Cost present[u-1]//2. Children use dp[v][1]
            u_buy_disc = [-float('inf')] * (budget + 1)
            cost_disc = cost_full // 2
            if cost_disc <= budget:
                u_buy_disc[cost_disc] = future[u - 1] - cost_disc

            for v in adj[u]:
                v_dp0, v_dp1 = dfs(v)
                
                next_not_buy = [-float('inf')] * (budget + 1)
                next_buy_full = [-float('inf')] * (budget + 1)
                next_buy_disc = [-float('inf')] * (budget + 1)
                
                for c in range(budget + 1):
                    if u_not_buy[c] == -float('inf') and u_buy_full[c] == -float('inf') and u_buy_disc[c] == -float('inf'):
                        continue
                    for cv in range(budget - c + 1):
                        # If u didn't buy, children use v_dp0
                        if u_not_buy[c] != -float('inf') and v_dp0[cv] != -float('inf'):
                            next_not_buy[c + cv] = max(next_not_buy[c + cv], u_not_buy[c] + v_dp0[cv])
                        # If u bought, children use v_dp1
                        if v_dp1[cv] != -float('inf'):
                            if u_buy_full[c] != -float('inf'):
                                next_buy_full[c + cv] = max(next_buy_full[c + cv], u_buy_full[c] + v_dp1[cv])
                            if u_buy_disc[c] != -float('inf'):
                                next_buy_disc[c + cv] = max(next_buy_disc[c + cv], u_buy_disc[c] + v_dp1[cv])
                
                u_not_buy, u_buy_full, u_buy_disc = next_not_buy, next_buy_full, next_buy_disc

            # Finalize dp0 and dp1 for node u
            for c in range(budget + 1):
                dp0[c] = max(u_not_buy[c], u_buy_full[c])
                dp1[c] = max(u_not_buy[c], u_buy_disc[c])
            
            return dp0, dp1

        res_dp0, _ = dfs(1)
        ans = max(res_dp0)
        return ans if ans > 0 else 0
# @lc code=end