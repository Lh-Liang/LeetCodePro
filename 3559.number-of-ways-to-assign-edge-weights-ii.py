import sys
from collections import deque

#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        LOG = 18
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        # BFS to compute depth and up[0]
        queue = deque([(1, 0, 0)])
        visited = [False] * (n + 1)
        visited[1] = True
        while queue:
            u, p, d = queue.popleft()
            up[0][u] = p
            depth[u] = d
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append((v, u, d + 1))
        
        # Fill binary lifting table
        for i in range(1, LOG):
            up_prev = up[i - 1]
            up_curr = up[i]
            for u in range(1, n + 1):
                up_curr[u] = up_prev[up_prev[u]]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[i][u]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                upi = up[i]
                if upi[u] != upi[v]:
                    u = upi[u]
                    v = upi[v]
            return up[0][u]
        
        MOD = 10**9 + 7
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
            else:
                lca = get_lca(u, v)
                dist = depth[u] + depth[v] - 2 * depth[lca]
                results.append(pow2[dist - 1])
        
        return results
# @lc code=end