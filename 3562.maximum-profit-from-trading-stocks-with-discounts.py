#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        from collections import defaultdict
        
        # Step 1: Build adjacency list for hierarchy.
        adj = defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)
        
        # Step 2: Recursive function with memoization.
        memo = {}
        def dfs(emp_id, remaining_budget):
            if emp_id > n:
                return 0
            if (emp_id, remaining_budget) in memo:
                return memo[(emp_id, remaining_budget)]
            
            # Profit without buying this employee's stock.
            max_profit = dfs(emp_id + 1, remaining_budget)
            
            # Profit when buying this employee's stock without discount.
            cost = present[emp_id - 1]
            if remaining_budget >= cost:
                profit_without_discount = future[emp_id - 1] - cost + dfs(emp_id + 1, remaining_budget - cost)
                max_profit = max(max_profit, profit_without_discount)
            
            # Check discount applicability for subordinates and apply DFS for them.
            for subordinate in adj[emp_id]:
                discounted_cost = present[subordinate - 1] // 2
                if remaining_budget >= discounted_cost:
                    # Apply discount and recurse for subordinate with updated budget
                    profit_with_discount = future[subordinate - 1] - discounted_cost + dfs(subordinate + 1, remaining_budget - discounted_cost)
                    max_profit = max(max_profit, profit_with_discount)
                    
            memo[(emp_id, remaining_budget)] = max_profit
            return max_profit
        
        # Step 3: Start DFS exploration from the first employee with full budget.
        return dfs(1, budget)
# @lc code=end