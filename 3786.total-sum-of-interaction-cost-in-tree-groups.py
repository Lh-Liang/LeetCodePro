#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        # Step 1: Count total occurrences of each group
        # Since group IDs are between 1 and 20, we use an array of size 21.
        total_group_counts = [0] * 21
        for g in group:
            total_group_counts[g] += 1
            
        # Step 2: Build the tree adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 3: BFS to determine parent pointers and processing order
        # We root the tree at node 0. 'order' will store nodes in BFS order.
        parent = [-1] * n
        order = [0]
        visited = [False] * n
        visited[0] = True
        
        head = 0
        while head < len(order):
            u = order[head]
            head += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    order.append(v)
        
        # Step 4: Calculate interaction costs
        # node_counts[u][g] will store the number of nodes of group g in the subtree rooted at u
        node_counts = [[0] * 21 for _ in range(n)]
        
        # Initialize counts with the node's own group
        for i in range(n):
            node_counts[i][group[i]] = 1
            
        ans = 0
        
        # Iterate in reverse BFS order (from leaves up to children of root)
        # This simulates a post-order traversal without recursion limits.
        # We skip the root (index 0 in 'order') because we process edges (u, parent[u]).
        for i in range(n - 1, 0, -1):
            u = order[i]
            p = parent[u]
            
            u_counts = node_counts[u]
            p_counts = node_counts[p]
            
            # For each group, calculate the contribution of the edge (u, p)
            for g in range(1, 21):
                c = u_counts[g]
                if c > 0:
                    # The edge (u, p) separates the tree into two parts for group g:
                    # 1. The subtree at u (containing c nodes of group g)
                    # 2. The rest of the tree (containing total_group_counts[g] - c nodes)
                    # The number of paths between pairs of group g crossing this edge is the product.
                    ans += c * (total_group_counts[g] - c)
                    
                    # Propagate counts up to the parent
                    p_counts[g] += c
                    
        return ans
# @lc code=end