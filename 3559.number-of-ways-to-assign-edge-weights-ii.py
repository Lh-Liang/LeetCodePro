#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
import sys

# Increase recursion depth for deep trees if using DFS
sys.setrecursionlimit(200000)

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary lifting preprocessing
        # LOG needs to be enough to cover N. 2^17 > 10^5
        LOG = 18
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # BFS to compute depth and parent (up[node][0])
        # Using BFS prevents recursion depth issues
        queue = [1]
        visited = [False] * (n + 1)
        visited[1] = True
        depth[1] = 0
        
        while queue:
            u = queue.pop(0)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    queue.append(v)
        
        # Fill binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                if up[i][j-1] != 0:
                    up[i][j] = up[up[i][j-1]][j-1]
                else:
                    up[i][j] = 0
                    
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            # Bring u to same depth as v
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = up[u][j]
            
            if u == v:
                return u
            
            # Lift both until just below LCA
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            
            return up[u][0]

        ans = []
        
        # Precompute powers of 2 to save time on pow calls inside loop
        # Max distance is n-1
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]
            
            # We need the number of ways to choose an ODD number of 1s.
            # Total edges = dist.
            # Number of ways = sum(C(dist, k) for odd k) = 2^(dist - 1)
            
            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])
                
        return ans
# @lc code=end