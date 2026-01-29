#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
from typing import List
from collections import defaultdict
import heapq
import math

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build adjacency list for hierarchy relationships
        adj = defaultdict(list)
        for u, v in hierarchy:
            adj[u - 1].append(v - 1)
        
        # Calculate potential profits and sort by profitability descending then cost ascending
        transactions = []
        for i in range(n):
            profit = future[i] - present[i]
            transactions.append((profit, present[i], i))
        
        # Sort transactions by descending profit and then ascending cost
        transactions.sort(key=lambda x: (-x[0], x[1]))
        
        total_profit = 0
        used_budget = 0
        purchased = [False] * n  # Tracks if an employee's stock is purchased or not
        
        # Process each transaction considering possible discounts due to hierarchy
        for profit, cost, employee in transactions:
            # Check if any boss purchased their own stock so this employee can get a discount
            discounted_cost = cost if not any(purchased[boss] for boss in adj[employee]) else math.floor(cost / 2)
            if used_budget + discounted_cost <= budget:
                used_budget += discounted_cost
                total_profit += future[employee] - discounted_cost  # Calculate actual realized profit after discount cost if applicable
                purchased[employee] = True  # Mark as purchased only if successfully bought within budget constraints
                
        return total_profit  # Return maximum achievable profit within given constraints of hierarchy and budget management.
# @lc code=end