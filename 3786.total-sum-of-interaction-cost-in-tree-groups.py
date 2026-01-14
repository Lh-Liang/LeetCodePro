#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        from collections import defaultdict, Counter
        
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Count total nodes per group
        total_group_counts = Counter(group)
        
        total_cost = 0
        
        # For each edge (u, v)
        for u, v in edges:
            # DFS from v without crossing back to u
            def dfs(node, parent):
                counts = Counter()
                counts[group[node]] = 1
                for neighbor in adj[node]:
                    if neighbor != parent:
                        sub_counts = dfs(neighbor, node)
                        counts.update(sub_counts)
                return counts
            
            # Count nodes on v's side (subtree rooted at v)
            v_side = dfs(v, u)
            
            # For each group, calculate contribution
            for g in v_side:
                u_side_count = total_group_counts[g] - v_side[g]
                total_cost += v_side[g] * u_side_count
        
        return total_cost
# @lc code=end