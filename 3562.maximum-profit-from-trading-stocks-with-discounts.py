#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
from typing import List
import math
from collections import defaultdict

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build the tree
        tree = defaultdict(list)
        for u, v in hierarchy:
            tree[u-1].append(v-1)  # 0-based indexing

        # DP[node][budget][parentBought] = max profit
        # parentBought: 0 - parent didn't buy, 1 - parent bought
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(node, b, parentBought):
            res = 0
            children = tree[node]
            # Option 1: Don't buy at this node
            # Just combine the best options for children, with parentBought=0
            sub_res0 = 0
            # For each child, recursively compute
            for child in children:
                best = 0
                # Distribute budget 'b' among children arbitrarily
                # To do this efficiently, use knapsack
                dp = [0] * (b+1)
                for c in children:
                    if c == child:
                        continue
                    ndp = dp[:]
                    for bi in range(b+1):
                        for used in range(bi+1):
                            ndp[bi] = max(ndp[bi], dp[bi-used] + dfs(c, used, 0))
                    dp = ndp
                # For current child, try all possible budget splits
                for used in range(b+1):
                    best = max(best, dfs(child, used, 0) + dp[b-used])
                sub_res0 = max(sub_res0, best)
            res = max(res, sub_res0)

            # Option 2: Buy at this node (if enough budget)
            buy_price = present[node] if not parentBought else math.floor(present[node] / 2)
            if b >= buy_price:
                profit = future[node] - buy_price
                # Now distribute remaining budget among children, with parentBought=1
                dp = [0] * (b - buy_price + 1)
                for child in children:
                    ndp = dp[:]
                    for bi in range(b - buy_price + 1):
                        for used in range(bi+1):
                            ndp[bi] = max(ndp[bi], dp[bi-used] + dfs(child, used, 1))
                    dp = ndp
                res = max(res, profit + max(dp))
            return res

        # To avoid TLE, use bottom-up DP
        # Actually, above is a reference. Let's use classical tree DP with knapsack
        def dp_tree(node, parentBought):
            # dp[budget] = max profit for this subtree, given budget, parentBought
            buy_price = present[node] if not parentBought else present[node] // 2
            profit_if_buy = future[node] - buy_price
            children = tree[node]
            # dp0: not buy at this node
            dp0 = [0] * (budget + 1)
            # For each child, combine DP with parentBought=0
            for child in children:
                child_dp = dp_tree(child, 0)
                ndp = [0] * (budget + 1)
                for b1 in range(budget + 1):
                    for b2 in range(b1 + 1):
                        ndp[b1] = max(ndp[b1], dp0[b1 - b2] + child_dp[b2])
                dp0 = ndp
            # dp1: buy at this node (if enough budget)
            dp1 = [0] * (budget + 1)
            if buy_price <= budget:
                dp1[buy_price] = profit_if_buy
                for child in children:
                    child_dp = dp_tree(child, 1)
                    ndp = [0] * (budget + 1)
                    for b1 in range(budget + 1):
                        for b2 in range(b1 + 1):
                            ndp[b1] = max(ndp[b1], dp1[b1 - b2] + child_dp[b2])
                    dp1 = ndp
            result = [0] * (budget + 1)
            for b in range(budget + 1):
                result[b] = max(dp0[b], dp1[b])
            return result

        dp_result = dp_tree(0, 0)
        return max(dp_result)
# @lc code=end