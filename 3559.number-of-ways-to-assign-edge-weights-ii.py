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
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS to compute depths and parents
        parent = [-1] * (n + 1)
        depth = [0] * (n + 1)
        q = deque([1])
        parent[1] = -1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
        
        # Binary lifting preprocessing
        LOG = n.bit_length()
        up = [[-1] * (LOG + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            up[i][0] = parent[i]
        
        for k in range(1, LOG + 1):
            for i in range(1, n + 1):
                if up[i][k - 1] != -1:
                    up[i][k] = up[up[i][k - 1]][k - 1]
                else:
                    up[i][k] = -1
        
        def lca(u: int, v: int) -> int:
            # Ensure u is deeper than or same as v
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u to same level as v
            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = up[u][k]
                diff >>= 1
                k += 1
            if u == v:
                return u
            # Lift both until their parents are equal
            for k in range(LOG, -1, -1):
                if up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return parent[u]
        
        # Precompute powers of two
        max_dist = n - 1
        pow_two = [1] * (max_dist + 1)
        for i in range(1, max_dist + 1):
            pow_two[i] = (pow_two[i - 1] * 2) % MOD
        
        ans = []
        for u, v in queries:
            anc = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[anc]
            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow_two[dist - 1]) 
        return ans
# @lc code=end