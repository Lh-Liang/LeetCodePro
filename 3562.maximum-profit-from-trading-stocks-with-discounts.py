#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        from collections import defaultdict
        from math import inf
        
        children = defaultdict(list)
        for u, v in hierarchy:
            children[u].append(v)
        
        NEG_INF = -inf
        memo = {}
        
        def combine_children(child_dps):
            result = [NEG_INF] * (budget + 1)
            result[0] = 0
            
            for dp0_c, dp1_c in child_dps:
                new_result = [NEG_INF] * (budget + 1)
                for prev_cost in range(budget + 1):
                    if result[prev_cost] == NEG_INF:
                        continue
                    for child_cost in range(budget + 1 - prev_cost):
                        total_cost = prev_cost + child_cost
                        if dp0_c[child_cost] != NEG_INF:
                            new_result[total_cost] = max(new_result[total_cost], result[prev_cost] + dp0_c[child_cost])
                        if dp1_c[child_cost] != NEG_INF:
                            new_result[total_cost] = max(new_result[total_cost], result[prev_cost] + dp1_c[child_cost])
                result = new_result
            
            return result
        
        def dfs(node, parent_bought):
            if (node, parent_bought) in memo:
                return memo[(node, parent_bought)]
            
            my_price = present[node - 1] // 2 if parent_bought else present[node - 1]
            my_profit = future[node - 1] - my_price
            
            kids = children[node]
            
            if not kids:
                dp0 = [NEG_INF] * (budget + 1)
                dp0[0] = 0
                
                dp1 = [NEG_INF] * (budget + 1)
                if my_price <= budget:
                    dp1[my_price] = my_profit
                
                memo[(node, parent_bought)] = (dp0, dp1)
                return (dp0, dp1)
            
            child_dp_no_disc = [dfs(child, False) for child in kids]
            child_dp_with_disc = [dfs(child, True) for child in kids]
            
            combined_0 = combine_children(child_dp_no_disc)
            dp0 = combined_0
            
            combined_1 = combine_children(child_dp_with_disc)
            dp1 = [NEG_INF] * (budget + 1)
            for cost in range(budget + 1):
                if cost >= my_price and combined_1[cost - my_price] != NEG_INF:
                    dp1[cost] = combined_1[cost - my_price] + my_profit
            
            memo[(node, parent_bought)] = (dp0, dp1)
            return (dp0, dp1)
        
        dp0, dp1 = dfs(1, False)
        
        result = 0
        for cost in range(budget + 1):
            if dp0[cost] != NEG_INF:
                result = max(result, dp0[cost])
            if dp1[cost] != NEG_INF:
                result = max(result, dp1[cost])
        
        return result
# @lc code=end