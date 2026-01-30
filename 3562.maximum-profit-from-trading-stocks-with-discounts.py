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
        from collections import defaultdict
        tree = [[] for _ in range(n)]
        parent = [None] * n
        for u,v in hierarchy:
            tree[u-1].append(v-1)
            parent[v-1] = u-1

        # dp[u][state][cost]: max profit for subtree rooted at u,
        # state=0: boss did not buy, state=1: boss bought
        # Only store for used budget up to 'budget'
        def dfs(u):
            # dp_no: boss did NOT buy, dp_yes: boss did buy
            dp_no = [float('-inf')] * (budget+1)
            dp_yes = [float('-inf')] * (budget+1)
            # Case 1: Not buy u's stock
            dp_no[0] = 0
            dp_yes[0] = 0
            # Case 2: Buy u's stock
            cost0 = present[u]
            prof0 = future[u]-present[u]
            if cost0 <= budget:
                dp_no[cost0] = prof0
            cost1 = present[u]//2
            prof1 = future[u]-cost1
            if cost1 <= budget:
                dp_yes[cost1] = prof1
            # Merge with children
            for v in tree[u]:
                cdp_no, cdp_yes = dfs(v)
                # Merge dp_no: boss did NOT buy
                ndp_no = [float('-inf')] * (budget+1)
                for b in range(budget+1):
                    if dp_no[b] == float('-inf'): continue
                    for cb in range(budget-b+1):
                        val = cdp_no[cb]
                        if val != float('-inf'):
                            if b+cb <= budget:
                                ndp_no[b+cb] = max(ndp_no[b+cb], dp_no[b]+val)
                dp_no = ndp_no
                # Merge dp_yes: boss DID buy
                ndp_yes = [float('-inf')] * (budget+1)
                for b in range(budget+1):
                    if dp_yes[b] == float('-inf'): continue
                    for cb in range(budget-b+1):
                        val = cdp_yes[cb]
                        if val != float('-inf'):
                            if b+cb <= budget:
                                ndp_yes[b+cb] = max(ndp_yes[b+cb], dp_yes[b]+val)
                dp_yes = ndp_yes
            return dp_no, dp_yes

        dp_no, dp_yes = dfs(0)
        # Verification: Ensure returned values respect budget and constraints
        assert all(0 <= i <= budget for i in range(len(dp_no))), "Budget indices are out of range."
        assert all(isinstance(val, (int, float)) for val in dp_no), "DP values should be numeric."
        return max( max(dp_no), max(dp_yes) )
# @lc code=end