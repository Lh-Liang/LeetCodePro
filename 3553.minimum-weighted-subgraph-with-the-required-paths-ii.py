#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
import sys

class Solution:
    def minimumWeight(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = n.bit_length()
        up = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist_to_root = [0] * n

        # Iterative DFS for tree properties
        stack = [(0, -1, 0, 0)]
        while stack:
            u, p, d, w_sum = stack.pop()
            up[0][u] = p
            depth[u] = d
            dist_to_root[u] = w_sum
            for v, w in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1, w_sum + w))

        # Binary lifting table
        for i in range(1, LOG):
            row = up[i]
            prev_row = up[i-1]
            for u in range(n):
                mid = prev_row[u]
                if mid != -1:
                    row[u] = prev_row[mid]

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
                if up[i][u] != up[i][v]:
                    u = up[i][u]
                    v = up[i][v]
            return up[0][u]

        def get_dist(u, v):
            lca = get_lca(u, v)
            return dist_to_root[u] + dist_to_root[v] - 2 * dist_to_root[lca]

        ans = []
        for s1, s2, d in queries:
            # The junction node X is the LCA with the greatest depth
            l12 = get_lca(s1, s2)
            l1d = get_lca(s1, d)
            l2d = get_lca(s2, d)
            
            x = l12
            if depth[l1d] > depth[x]: x = l1d
            if depth[l2d] > depth[x]: x = l2d
            
            # Total weight = dist(s1, x) + dist(s2, x) + dist(d, x)
            res = get_dist(s1, x) + get_dist(s2, x) + get_dist(d, x)
            ans.append(res)
            
        return ans
# @lc code=end