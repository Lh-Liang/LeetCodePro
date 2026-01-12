#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
import sys
from typing import List

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Count total nodes in each group. 
        # group[i] is between 1 and 20.
        group_counts = [0] * 21
        for g in group:
            group_counts[g] += 1
            
        total_cost = 0
        
        # subtree_group_counts[u] will store the number of nodes of each group in subtree u
        # To save memory and time, we perform a DFS and calculate contribution on the fly.
        def dfs(u, p):
            nonlocal total_cost
            # current_counts[g] = nodes of group g in subtree u
            current_counts = [0] * 21
            current_counts[group[u]] = 1
            
            for v in adj[u]:
                if v == p:
                    continue
                child_counts = dfs(v, u)
                for g in range(1, 21):
                    if child_counts[g] > 0:
                        # Number of nodes of group g in subtree v vs outside subtree v
                        in_subtree = child_counts[g]
                        out_subtree = group_counts[g] - in_subtree
                        total_cost += in_subtree * out_subtree
                        current_counts[g] += child_counts[g]
            
            return current_counts

        dfs(0, -1)
        return total_cost
# @lc code=end