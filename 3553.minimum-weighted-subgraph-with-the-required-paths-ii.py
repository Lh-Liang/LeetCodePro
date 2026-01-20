#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Preprocessing for LCA using Binary Lifting
        # depth_node: depth in terms of number of edges (for LCA logic)
        # depth_weight: depth in terms of sum of weights (for distance calculation)
        depth_node = [0] * n
        depth_weight = [0] * n
        LOG = 18  # Sufficient for 10^5 nodes
        up = [[-1] * LOG for _ in range(n)]
        
        # DFS to build tree structure rooted at 0
        stack = [(0, -1, 0, 0)] # u, p, d_node, d_weight
        
        # Iterative DFS to avoid recursion limit issues and overhead
        # But we need to process in topological order for 'up' table or do it after
        # Standard recursive DFS is easier to write, let's use iterative for safety with large N
        
        parent = [-1] * n
        
        # BFS or DFS to set parents and depths
        queue = [0]
        visited = [False] * n
        visited[0] = True
        
        # Using BFS for level order traversal to setup depths
        q_idx = 0
        while q_idx < len(queue):
            u = queue[q_idx]
            q_idx += 1
            
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth_node[v] = depth_node[u] + 1
                    depth_weight[v] = depth_weight[u] + w
                    queue.append(v)
        
        # Build Binary Lifting Table
        for i in range(n):
            up[i][0] = parent[i]
        
        for j in range(1, LOG):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
                else:
                    up[i][j] = -1
                    
        def get_lca(u, v):
            if depth_node[u] < depth_node[v]:
                u, v = v, u
            
            # Lift u to the same depth as v
            diff = depth_node[u] - depth_node[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            
            if u == v:
                return u
            
            # Lift both until they are just below LCA
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            
            return up[u][0]

        def get_dist(u, v):
            lca = get_lca(u, v)
            return depth_weight[u] + depth_weight[v] - 2 * depth_weight[lca]

        results = []
        for src1, src2, dest in queries:
            # The minimum weight subgraph connecting src1, src2, dest is unique.
            # The sum of weights of edges in this subgraph is:
            # (dist(src1, src2) + dist(src1, dest) + dist(src2, dest)) // 2
            
            d12 = get_dist(src1, src2)
            d1d = get_dist(src1, dest)
            d2d = get_dist(src2, dest)
            
            ans = (d12 + d1d + d2d) // 2
            results.append(ans)
            
        return results
# @lc code=end