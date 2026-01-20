from collections import deque
from typing import List

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        parent = [-1] * n
        depth = [0] * n
        dist = [0] * n
        LOG = 18  # Sufficient for 10^5 nodes
        up = [[-1] * LOG for _ in range(n)]
        
        # BFS to build the tree structure (parent, depth, dist)
        queue = deque([0])
        # Standard BFS
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    queue.append(v)
        
        # Initialize binary lifting table
        for u in range(n):
            up[u][0] = parent[u]
            
        for i in range(1, LOG):
            for u in range(n):
                if up[u][i-1] != -1:
                    up[u][i] = up[up[u][i-1]][i-1]
                else:
                    up[u][i] = -1
                    
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            
            if u == v:
                return u
            
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            
            return up[u][0]

        ans = []
        for u, v in queries:
            lca = get_lca(u, v)
            total_dist = dist[u] + dist[v] - 2 * dist[lca]
            dist_u_lca = dist[u] - dist[lca]
            
            # Check if the median is on the path segment u -> lca
            # We check if dist(u, lca) >= total_dist / 2
            if 2 * dist_u_lca >= total_dist:
                target_2dist = 2 * dist[u] - total_dist
                # We want the node x closest to u (deepest) such that 2*dist[x] <= target_2dist.
                # Check if u itself is the answer
                if 2 * dist[u] <= target_2dist:
                    ans.append(u)
                else:
                    # Lift u to the highest node that is INVALID (2*dist > target)
                    # The parent of that node will be the first VALID node (closest to u)
                    curr = u
                    for i in range(LOG - 1, -1, -1):
                        if up[curr][i] != -1:
                            if 2 * dist[up[curr][i]] > target_2dist:
                                curr = up[curr][i]
                    ans.append(up[curr][0])
            else:
                # Median is on path segment lca -> v
                # We want the node x closest to lca (shallowest) such that dist(u, x) >= total_dist / 2
                # Equivalent to: 2*dist[x] >= total_dist - 2*dist[u] + 4*dist[lca]
                target_2dist = total_dist - 2 * dist[u] + 4 * dist[lca]
                
                # We want the highest ancestor of v that satisfies the condition (VALID)
                # Lift v as long as the destination is VALID
                curr = v
                for i in range(LOG - 1, -1, -1):
                    if up[curr][i] != -1:
                        if 2 * dist[up[curr][i]] >= target_2dist:
                            curr = up[curr][i]
                ans.append(curr)
        
        return ans