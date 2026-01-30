#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
from typing import List
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        import sys
        sys.setrecursionlimit(1 << 20)
        LOG = 17  # Since n <= 1e5, 2^17 > 1e5
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [[-1] * n for _ in range(LOG)]
        weight = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        cumw = [0] * n

        def dfs(u, p):
            for v, w in adj[u]:
                if v == p:
                    continue
                parent[0][v] = u
                weight[0][v] = w
                depth[v] = depth[u] + 1
                cumw[v] = cumw[u] + w
                dfs(v, u)
        dfs(0, -1)

        for k in range(1, LOG):
            for v in range(n):
                if parent[k-1][v] != -1:
                    parent[k][v] = parent[k-1][parent[k-1][v]]
                    weight[k][v] = weight[k-1][v] + weight[k-1][parent[k-1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and depth[parent[k][u]] >= depth[v]:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG-1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        # Build path from u to v (inclusive), going up to lca and then down to v
        def build_path(u, v, ancestor):
            path_up = []  # u to lca (excluding lca)
            x = u
            while x != ancestor:
                path_up.append(x)
                x = parent[0][x]
            path_down = []  # v to lca (excluding lca)
            y = v
            while y != ancestor:
                path_down.append(y)
                y = parent[0][y]
            full_path = path_up + [ancestor] + path_down[::-1]  # from u to v, inclusive
            return full_path

        res = []
        for u, v in queries:
            ancestor = lca(u, v)
            total = cumw[u] + cumw[v] - 2 * cumw[ancestor]
            half = total / 2
            path = build_path(u, v, ancestor)
            curr_sum = 0
            prev = path[0]
            found = False
            for idx, node in enumerate(path):
                if idx == 0:
                    curr_sum = 0
                else:
                    # edge weight between prev and node
                    w = abs(cumw[node] - cumw[prev])
                    curr_sum += w
                # Check weighted median condition
                if curr_sum >= half and not found:
                    # Explicitly verify the weighted median condition
                    res.append(node)
                    found = True
                    break
                prev = node
            if not found:
                # As a safeguard, check that the last node (must be v) is valid
                res.append(path[-1])
        return res
# @lc code=end