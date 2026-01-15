#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        # Binary lifting setup
        LOG = n.bit_length()
        parent = [[0] * (LOG + 1) for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # BFS to compute depth and parent
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        parent[1][0] = 1
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[node] + 1
                    parent[neighbor][0] = node
                    queue.append(neighbor)
        
        # Fill binary lifting table
        for j in range(1, LOG + 1):
            for i in range(1, n + 1):
                parent[i][j] = parent[parent[i][j-1]][j-1]
        
        # LCA function
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG + 1):
                if (diff >> j) & 1:
                    u = parent[u][j]
            if u == v:
                return u
            for j in range(LOG, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]
            return parent[u][0]
        
        # Process queries
        result = []
        for u, v in queries:
            if u == v:
                result.append(0)
            else:
                l = lca(u, v)
                path_length = depth[u] + depth[v] - 2 * depth[l]
                result.append(pow2[path_length - 1])
        
        return result
# @lc code=end