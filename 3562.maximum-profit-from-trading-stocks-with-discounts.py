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
        
        INF = -10**9
        self.dp = [[[INF] * (budget + 1) for _ in range(2)] for _ in range(n + 1)]
        self.budget = budget
        self.present = present
        self.future = future
        self.adj = adj
        
        def dfs(u: int) -> None:
            children = self.adj[u]
            for v in children:
                dfs(v)
            
            # Compute child_dp[disc][j]: max profit from children with child discount 'disc', spending j
            child_dp = [[INF] * (self.budget + 1) for _ in range(2)]
            for disc in range(2):
                temp = [INF] * (self.budget + 1)
                temp[0] = 0
                for v in children:
                    new_temp = [INF] * (self.budget + 1)
                    dpv = self.dp[v][disc]
                    for s in range(self.budget + 1):
                        if temp[s] == INF:
                            continue
                        for a in range(self.budget - s + 1):
                            if dpv[a] != INF:
                                ns = s + a
                                if ns > self.budget:
                                    break
                                new_temp[ns] = max(new_temp[ns], temp[s] + dpv[a])
                    temp = new_temp
                child_dp[disc] = temp
            
            # Now for each discount d for u
            for d in range(2):
                p_idx = u - 1
                # No buy: cost=0, prof=0, child_disc=0
                for j in range(self.budget + 1):
                    if child_dp[0][j] != INF:
                        m = j
                        self.dp[u][d][m] = max(self.dp[u][d][m], child_dp[0][j])
                
                # Buy: compute cost and prof, child_disc=1
                p = self.present[p_idx]
                f = self.future[p_idx]
                cost = p // 2 if d == 1 else p
                prof = f - cost
                for j in range(self.budget + 1):
                    if child_dp[1][j] != INF:
                        m = cost + j
                        if m <= self.budget:
                            self.dp[u][d][m] = max(self.dp[u][d][m], prof + child_dp[1][j])
        
        dfs(1)
        
        ans = 0
        for m in range(self.budget + 1):
            ans = max(ans, self.dp[1][0][m])
        return ans

# @lc code=end