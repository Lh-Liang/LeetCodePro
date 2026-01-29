#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
import sys

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Standard binary lifting for LCA
        LOG = n.bit_length()
        up = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        w_depth = [0] * n
        
        # Iterative DFS to avoid recursion limit issues and handle large trees
        stack = [(0, -1, 0, 0)]
        while stack:
            u, p, d, wd = stack.pop()
            depth[u] = d
            w_depth[u] = wd
            up[u][0] = p
            for v, w in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1, wd + w))

        for j in range(1, LOG):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        def get_dist(u, v):
            lca = get_lca(u, v)
            return w_depth[u] + w_depth[v] - 2 * w_depth[lca]

        results = []
        for s1, s2, d in queries:
            d12 = get_dist(s1, s2)
            d2d = get_dist(s2, d)
            d1d = get_dist(s1, d)
            # Steiner Tree weight for 3 nodes in a tree
            results.append((d12 + d2d + d1d) // 2)
            
        return results
# @lc code=end