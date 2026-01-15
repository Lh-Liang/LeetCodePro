#
# @lc app=leetcode id=3530 lang=python3
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

from typing import List
from collections import deque
import heapq

# @lc code=start
class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        # Build adjacency list and indegree array.
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1
        
        # We need to consider all topological orders and maximize profit.
        # Since n <= 22, we can use DP over subsets (bitmask).
        # dp[mask] = maximum profit achievable when we have processed nodes in mask.
        # We can process nodes one by one. For a given mask, the next node to add must have all its prerequisites already in mask.
        # Let cnt = number of nodes already processed (popcount of mask). Then position for new node is cnt+1 (1-based).
        # So profit added = score[node] * (cnt+1).
        # We want dp[full_mask] where full_mask = (1<<n)-1.
        
        full_mask = (1 << n) - 1
        dp = [-10**18] * (1 << n)
        dp[0] = 0
        
        # Precompute prerequisite masks for each node: nodes that must be processed before it.
        preMask = [0] * n
        for u, v in edges:
            preMask[v] |= (1 << u)  # v requires u.
        
        # Iterate over all masks from 0 to full_mask.
        for mask in range(full_mask + 1):
            if dp[mask] < 0:
                continue  # unreachable state.
            cnt = bin(mask).count('1')  # number of processed nodes.
            next_pos = cnt + 1  # position for next node.
            # For each node not in mask, check if all prerequisites are satisfied.
            for node in range(n):
                if mask & (1 << node):
                    continue
                if (preMask[node] & mask) == preMask[node]:
                    new_mask = mask | (1 << node)
                    new_profit = dp[mask] + score[node] * next_pos
                    if new_profit > dp[new_mask]:
                        dp[new_mask] = new_profit
        
        return dp[full_mask]
# @lc code=end