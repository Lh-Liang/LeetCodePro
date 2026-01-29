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
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        LOG = 18
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        
        # BFS to compute depth and binary lifting parent (up[0])
        # Using BFS to avoid recursion depth issues in Python
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[0][v] = u
                    queue.append(v)
        
        # Precompute binary lifting table
        for i in range(1, LOG):
            upi = up[i]
            up_prev = up[i-1]
            for v in range(1, n + 1):
                upi[v] = up_prev[up_prev[v]]
        
        MOD = 10**9 + 7
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
                continue
            
            # Find LCA(u, v) using binary lifting
            curr_u, curr_v = u, v
            if depth[curr_u] < depth[curr_v]:
                curr_u, curr_v = curr_v, curr_u
            
            diff = depth[curr_u] - depth[curr_v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    curr_u = up[i][curr_u]
            
            if curr_u == curr_v:
                lca = curr_u
            else:
                for i in range(LOG - 1, -1, -1):
                    upi = up[i]
                    if upi[curr_u] != upi[curr_v]:
                        curr_u = upi[curr_u]
                        curr_v = upi[curr_v]
                lca = up[0][curr_u]
            
            # Path length L is the number of edges
            dist = depth[u] + depth[v] - 2 * depth[lca]
            # Number of ways = 2^(dist-1) mod MOD for dist >= 1
            results.append(pow2[dist - 1])
        
        return results
# @lc code=end