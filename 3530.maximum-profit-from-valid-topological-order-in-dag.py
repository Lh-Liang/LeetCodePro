#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        from functools import lru_cache
        
        # Build adjacency list - store predecessors for each node
        predecessors = [set() for _ in range(n)]
        for u, v in edges:
            predecessors[v].add(u)
        
        # DP with memoization
        @lru_cache(maxsize=None)
        def solve(mask):
            # If all nodes processed
            if mask == (1 << n) - 1:
                return 0
            
            # Count how many nodes are in the mask
            position = bin(mask).count('1') + 1  # Next position (1-based)
            
            max_profit = 0
            
            # Try adding each unprocessed node
            for node in range(n):
                if mask & (1 << node):  # Already processed
                    continue
                
                # Check if all predecessors are processed
                can_add = all((mask & (1 << pred)) for pred in predecessors[node])
                
                if can_add:
                    # Add this node at current position
                    profit = score[node] * position + solve(mask | (1 << node))
                    max_profit = max(max_profit, profit)
            
            return max_profit
        
        return solve(0)
# @lc code=end