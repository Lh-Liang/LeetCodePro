#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        import sys
        sys.setrecursionlimit(1 << 20)
        MOD = 10 ** 9 + 7

        n = len(edges) + 1
        # Build tree
        tree = [[] for _ in range(n + 1)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        LOG = 17  # since n <= 1e5, log2(1e5) ~= 17
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        def dfs(u, p):
            parent[0][u] = p
            for v in tree[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)
        dfs(1, -1)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        def odd_ways(L):
            if L == 0:
                return 0
            return pow(2, L - 1, MOD)

        res = []
        for u, v in queries:
            if u == v:
                res.append(0)
            else:
                anc = lca(u, v)
                L = depth[u] + depth[v] - 2 * depth[anc]
                # Sanity check: L should be >= 1 and <= n-1
                if not (0 <= L < n):
                    res.append(0)
                    continue
                res.append(odd_ways(L))
        return res
# @lc code=end