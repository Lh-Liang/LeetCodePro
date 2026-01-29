#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        LOG = 18
        parent = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        vis = [False] * (n + 1)
        q = deque([1])
        vis[1] = True
        parent[1][0] = 1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    depth[v] = depth[u] + 1
                    parent[v][0] = u
                    q.append(v)
        for j in range(1, LOG):
            for i in range(1, n + 1):
                parent[i][j] = parent[parent[i][j - 1]][j - 1]
        def get_lca(u, v):
            if depth[u] > depth[v]:
                u, v = v, u
            diff = depth[v] - depth[u]
            j = 0
            while diff > 0:
                if diff & 1:
                    v = parent[v][j]
                diff >>= 1
                j += 1
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]
            return parent[u][0]
        ans = []
        for qu, qv in queries:
            l = get_lca(qu, qv)
            k = depth[qu] + depth[qv] - 2 * depth[l]
            ans.append(0 if k == 0 else pow(2, k - 1, MOD))
        return ans

# @lc code=end