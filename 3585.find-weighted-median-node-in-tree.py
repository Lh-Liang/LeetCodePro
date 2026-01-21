#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
from typing import List

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        LOG = 18
        up = [[-1] * LOG for _ in range(n)]
        dist = [0] * n
        depth = [0] * n
        
        # Iterative DFS to compute dist, depth, and the first parent
        stack = [(0, -1, 0, 0)]
        while stack:
            u, p, d, dep = stack.pop()
            up[u][0] = p
            dist[u] = d
            depth[u] = dep
            for v, w in adj[u]:
                if v != p:
                    stack.append((v, u, d + w, dep + 1))
        
        # Fill binary lifting table
        for k in range(1, LOG):
            for i in range(n):
                if up[i][k-1] != -1:
                    up[i][k] = up[up[i][k-1]][k-1]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG - 1, -1, -1):
                if depth[u] - (1 << k) >= depth[v]:
                    u = up[u][k]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return up[u][0]
        
        results = []
        for u, v in queries:
            if u == v:
                results.append(u)
                continue
            
            lca = get_lca(u, v)
            total_w = dist[u] + dist[v] - 2 * dist[lca]
            
            # Check if median is on the path from u to lca
            if 2 * (dist[u] - dist[lca]) >= total_w:
                # If the first edge is already >= total_w / 2, or no edge exists
                curr = u
                for k in range(LOG - 1, -1, -1):
                    anc = up[curr][k]
                    if anc != -1 and depth[anc] >= depth[lca]:
                        if 2 * (dist[u] - dist[anc]) < total_w:
                            curr = anc
                results.append(up[curr][0])
            else:
                # Median is on the path from lca to v
                # Condition: D(u, lca) + D(lca, x) >= total_w / 2
                # (dist[u] - dist[lca]) + (dist[x] - dist[lca]) >= total_w / 2
                # 2*dist[u] - 4*dist[lca] + 2*dist[x] >= total_w
                target2 = total_w - 2 * dist[u] + 4 * dist[lca]
                curr = v
                for k in range(LOG - 1, -1, -1):
                    anc = up[curr][k]
                    if anc != -1 and depth[anc] >= depth[lca] and 2 * dist[anc] >= target2:
                        curr = anc
                results.append(curr)
                
        return results
# @lc code=end