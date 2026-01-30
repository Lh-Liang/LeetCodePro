#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
from typing import List
class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        import sys
        sys.setrecursionlimit(1 << 20)
        n = len(edges) + 1
        tree = [[] for _ in range(n)]
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))

        LOG = 17
        up = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        sum_w = [0] * n
        def dfs(u, p):
            up[0][u] = p
            for v, w in tree[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    sum_w[v] = sum_w[u] + w
                    dfs(v, u)
        dfs(0, -1)
        for k in range(1, LOG):
            for v in range(n):
                if up[k-1][v] != -1:
                    up[k][v] = up[k-1][up[k-1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG-1, -1, -1):
                if up[k][u] != -1 and depth[up[k][u]] >= depth[v]:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG-1, -1, -1):
                if up[k][u] != -1 and up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        res = []
        for src1, src2, dest in queries:
            lca1 = lca(src1, dest)
            lca2 = lca(src2, dest)
            lca12 = lca(src1, src2)
            lca_common = lca(lca1, src2)
            # Actually, we want the union of paths src1-dest and src2-dest
            # The total weight is sum_w[src1] + sum_w[src2] + sum_w[dest] 
            # minus the weights backtracked along their common ancestors
            ancestor = lca(lca1, lca2)
            total = sum_w[src1] + sum_w[src2] + sum_w[dest]
            total -= sum_w[lca1] + sum_w[lca2] + sum_w[ancestor]
            res.append(total)
        return res
# @lc code=end