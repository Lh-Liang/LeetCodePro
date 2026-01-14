#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build adjacency list
        children = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            children[u].append(v)
        
        memo = {}
        
        def merge_dp(dp1, dp2):
            merged = [0] * (budget + 1)
            for b in range(budget + 1):
                for b1 in range(b + 1):
                    merged[b] = max(merged[b], dp1[b1] + dp2[b - b1])
            return merged
        
        def dfs(u, parent_bought):
            if (u, parent_bought) in memo:
                return memo[(u, parent_bought)]
            
            cost_u = present[u - 1]
            if parent_bought:
                cost_u //= 2
            profit_u = future[u - 1] - cost_u
            
            # Get children's DP assuming u doesn't buy
            children_no_buy = [0] * (budget + 1)
            for child in children[u]:
                child_dp = dfs(child, False)
                children_no_buy = merge_dp(children_no_buy, child_dp)
            
            # Get children's DP assuming u buys
            children_buy = [0] * (budget + 1)
            for child in children[u]:
                child_dp = dfs(child, True)
                children_buy = merge_dp(children_buy, child_dp)
            
            # Compute final DP
            dp = [0] * (budget + 1)
            for b in range(budget + 1):
                # Option 1: Don't buy u
                dp[b] = children_no_buy[b]
                
                # Option 2: Buy u
                if b >= cost_u:
                    dp[b] = max(dp[b], profit_u + children_buy[b - cost_u])
            
            memo[(u, parent_bought)] = dp
            return dp
        
        result_dp = dfs(1, False)
        return result_dp[budget]
# @lc code=end