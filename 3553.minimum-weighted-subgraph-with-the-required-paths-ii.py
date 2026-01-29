#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        LOG = 18
        parent = [[-1] * LOG for _ in range(n)]
        hop_depth = [0] * n
        weighted_depth = [0] * n
        vis = [False] * n
        q = deque([0])
        vis[0] = True
        parent[0][0] = 0
        while q:
            u = q.popleft()
            for v, w in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    parent[v][0] = u
                    hop_depth[v] = hop_depth[u] + 1
                    weighted_depth[v] = weighted_depth[u] + w
                    q.append(v)
        for j in range(1, LOG):
            for i in range(n):
                p = parent[i][j - 1]
                if p != -1:
                    parent[i][j] = parent[p][j - 1]
                else:
                    parent[i][j] = -1
        def get_lca(u: int, v: int) -> int:
            du = hop_depth[u]
            dv = hop_depth[v]
            if du > dv:
                u, v = v, u
                du, dv = dv, du
            diff = dv - du
            for j in range(LOG):
                if (diff >> j) & 1:
                    v = parent[v][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]
            return parent[u][0]
        def get_dist(u: int, v: int) -> int:
            l = get_lca(u, v)
            return weighted_depth[u] + weighted_depth[v] - 2 * weighted_depth[l]
        ans = []
        for src1, src2, dest in queries:
            a, b, c = src1, src2, dest
            lca_ab = get_lca(a, b)
            lca_ac = get_lca(a, c)
            lca_bc = get_lca(b, c)
            cands = [(hop_depth[lca_ab], lca_ab), (hop_depth[lca_ac], lca_ac), (hop_depth[lca_bc], lca_bc)]
            _, m = max(cands)
            total = get_dist(a, m) + get_dist(b, m) + get_dist(c, m)
            ans.append(total)
        return ans

# @lc code=end