#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
from typing import List

import sys

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for ui, vi, wi in edges:
            adj[ui].append((vi, wi))
            adj[vi].append((ui, wi))

        LOG = 18
        parent = [[-1] * n for _ in range(LOG)]
        dist_to_anc = [[0] * n for _ in range(LOG)]
        level = [0] * n
        weighted_depth = [0] * n

        def dfs(node: int, par: int, lev: int, wdep: int, edgew: int) -> None:
            parent[0][node] = par
            dist_to_anc[0][node] = edgew
            level[node] = lev
            weighted_depth[node] = wdep
            for nei, w in adj[node]:
                if nei != par:
                    dfs(nei, node, lev + 1, wdep + w, w)

        sys.setrecursionlimit(100010)
        dfs(0, -1, 0, 0, 0)

        # Build binary lifting tables
        for k in range(1, LOG):
            for i in range(n):
                if parent[k - 1][i] != -1:
                    p = parent[k - 1][i]
                    parent[k][i] = parent[k - 1][p]
                    dist_to_anc[k][i] = dist_to_anc[k - 1][i] + dist_to_anc[k - 1][p]

        def get_lca(a: int, b: int) -> int:
            if level[a] > level[b]:
                a, b = b, a
            # Equalize levels
            for k in range(LOG):
                if (level[b] - level[a]) & (1 << k):
                    b = parent[k][b]
            if a == b:
                return a
            # Lift both
            for k in range(LOG - 1, -1, -1):
                if (parent[k][a] != parent[k][b] and
                    parent[k][a] != -1 and parent[k][b] != -1):
                    a = parent[k][a]
                    b = parent[k][b]
            return parent[0][a]

        ans = []
        for qu, qv in queries:
            if qu == qv:
                ans.append(qu)
                continue
            anc = get_lca(qu, qv)
            du = weighted_depth[qu] - weighted_depth[anc]
            dv = weighted_depth[qv] - weighted_depth[anc]
            total = du + dv
            thresh = (total + 1) // 2
            if du >= thresh:
                # Up lift from qu
                current = qu
                traveled = 0
                for k in range(LOG - 1, -1, -1):
                    if (parent[k][current] != -1 and
                        traveled + dist_to_anc[k][current] < thresh):
                        traveled += dist_to_anc[k][current]
                        current = parent[k][current]
                median = parent[0][current]
            else:
                remaining = thresh - du
                max_up = dv - remaining
                current = qv
                traveled = 0
                for k in range(LOG - 1, -1, -1):
                    if (parent[k][current] != -1 and
                        traveled + dist_to_anc[k][current] <= max_up):
                        traveled += dist_to_anc[k][current]
                        current = parent[k][current]
                median = current
            ans.append(median)
        return ans

# @lc code=end