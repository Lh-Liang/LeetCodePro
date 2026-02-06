#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        from collections import defaultdict, deque
        
        # Step 1: Create graph representation of hierarchy
        boss_map = defaultdict(list)
        for u, v in hierarchy:
            boss_map[u].append(v)
        
        # Step 2: Calculate initial profits without discounts as baseline
        profits = [(future[i] - present[i], i + 1) for i in range(n)] # Adjust index for employee ID
        
        # Step 3: Calculate discounted prices based on hierarchy using BFS traversal
        def get_discounted_prices():
            discounted_present = present[:]
            queue = deque([1]) # Start BFS with CEO (Employee ID 1)
            visited = set()
            purchased = set() # Track which employees have purchased stocks
            while queue:
                boss = queue.popleft()
                if boss not in visited:
                    visited.add(boss)
                    for subordinate in boss_map[boss]:
                        # Check if boss has purchased their stock before applying discount to subordinates
                        if boss in purchased:
                            discounted_present[subordinate - 1] = present[subordinate - 1] // 2 
                        queue.append(subordinate)
                    # Decide if boss should buy their own stock based on maximizing overall gain including subordinates' discounts.
                    # Add logic here to determine purchase based on current strategy and mark as purchased if chosen.
            return discounted_present
        
        discounted_present = get_discounted_prices()
        
        # Step 4: Use dynamic programming approach to maximize profit under budget constraints including possible discounts.
        dp = [0] * (budget + 1)
        profits.sort(reverse=True, key=lambda x: x[0]) # Sort by profit descending order after discount application strategy applied.		for potential_profit, emp_id in profits:			cost = discounted_present[emp_id - 1]			for b in range(budget, cost - 1, -1):				if cost <= b:					dp[b] = max(dp[b], dp[b - cost] + potential_profit )	return dp[budget]
n# @lc code=end