#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        dep = [0] * (n + 1)
        LOG = 18
        par = [[0] * LOG for _ in range(n + 1)]
        vis = [False] * (n + 1)
        
        q = deque([1])
        vis[1] = True
        par[1][0] = 1
        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                if not vis[nei]:
                    vis[nei] = True
                    dep[nei] = dep[cur] + 1
                    par[nei][0] = cur
                    q.append(nei)
        
        for j in range(1, LOG):
            for i in range(1, n + 1):
                par[i][j] = par[par[i][j - 1]][j - 1]
        
        def get_lca(u: int, v: int) -> int:
            if dep[u] > dep[v]:
                u, v = v, u
            # Level v to same depth as u
            for j in range(LOG):
                if ((dep[v] - dep[u]) & (1 << j)):
                    v = par[v][j]
            if u == v:
                return u
            # Jump
            for j in range(LOG - 1, -1, -1):
                if par[u][j] != par[v][j]:
                    u = par[u][j]
                    v = par[v][j]
            return par[u][0]
        
        ans = []
        for ui, vi in queries:
            l = get_lca(ui, vi)
            k = dep[ui] + dep[vi] - 2 * dep[l]
            if k == 0:
                ans.append(0)
            else:
                ans.append(pow(2, k - 1, MOD))
        return ans
# @lc code=end
