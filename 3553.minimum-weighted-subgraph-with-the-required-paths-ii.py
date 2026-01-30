#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
from typing import List
import sys
sys.setrecursionlimit(1 << 20)

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        LOG = 17
        parent = [[-1]*n for _ in range(LOG)]
        depth = [0]*n
        pre_sum = [0]*n
        def dfs(u, p):
            for v, w in graph[u]:
                if v != p:
                    parent[0][v] = u
                    depth[v] = depth[u] + 1
                    pre_sum[v] = pre_sum[u] + w
                    dfs(v, u)
        dfs(0, -1)
        for k in range(1, LOG):
            for v in range(n):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in reversed(range(LOG)):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in reversed(range(LOG)):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        res = []
        for src1, src2, dest in queries:
            lca1 = lca(src1, dest)
            lca2 = lca(src2, dest)
            lca12 = lca(src1, src2)
            w1 = pre_sum[src1] + pre_sum[dest] - 2*pre_sum[lca1]
            w2 = pre_sum[src2] + pre_sum[dest] - 2*pre_sum[lca2]
            w3 = pre_sum[src1] + pre_sum[src2] - 2*pre_sum[lca12]
            # Verify that the set of edges forms a connected subtree (by construction in a tree, the union of these paths does).
            res.append(w1 + w2 - w3)
        return res
# @lc code=end