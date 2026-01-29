#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def interactionCosts(self, n: int, edges: list[list[int]], group: list[int]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Identify unique groups and map them to 0-indexed values
        unique_groups = sorted(list(set(group)))
        group_map = {g: i for i, g in enumerate(unique_groups)}
        num_groups = len(unique_groups)
        
        # Total nodes in each group
        group_totals = [0] * num_groups
        for g in group:
            group_totals[group_map[g]] += 1
            
        total_interaction_cost = 0
        
        # subtree_counts[u][g] will store number of nodes of group g in subtree of u
        # To save memory, we calculate contribution on the fly during DFS
        def dfs(u, p):
            nonlocal total_interaction_cost
            # current_counts stores counts for the current subtree
            current_counts = [0] * num_groups
            current_counts[group_map[group[u]]] = 1
            
            for v in adj[u]:
                if v == p:
                    continue
                child_counts = dfs(v, u)
                for g_idx in range(num_groups):
                    # Edge (u, v) contribution for group g_idx:
                    # nodes_in_v_subtree * nodes_outside_v_subtree
                    count_in = child_counts[g_idx]
                    count_out = group_totals[g_idx] - count_in
                    total_interaction_cost += count_in * count_out
                    current_counts[g_idx] += count_in
            
            return current_counts

        dfs(0, -1)
        return total_interaction_cost
# @lc code=end