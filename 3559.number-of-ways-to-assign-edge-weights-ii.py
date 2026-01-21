#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
import collections
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Binary Lifting Precomputation
        LOG = n.bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [-1] * (n + 1)
        
        # BFS to find depths and parents
        queue = collections.deque([1])
        depth[1] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if depth[v] == -1:
                    depth[v] = depth[u] + 1
                    up[0][v] = u
                    queue.append(v)
        
        # Build the binary lifting table
        for i in range(1, LOG):
            prev_row = up[i-1]
            curr_row = up[i]
            for u in range(1, n + 1):
                curr_row[u] = prev_row[prev_row[u]]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u to same depth as v
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[i][u]
            if u == v:
                return u
            # Lift u and v together until they meet
            for i in range(LOG - 1, -1, -1):
                if up[i][u] != up[i][v]:
                    u = up[i][u]
                    v = up[i][v]
            return up[0][u]
        
        MOD = 10**9 + 7
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
            else:
                lca = get_lca(u, v)
                dist = depth[u] + depth[v] - 2 * depth[lca]
                # Number of ways is 2^(dist-1) mod 10^9 + 7
                results.append(pow2[dist - 1])
                
        return results
# @lc code=end