#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        LOG = 18
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        par = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        dist = [0] * n
        sum_up = [[0] * LOG for _ in range(n)]
        visited = [False] * n
        q = deque([0])
        visited[0] = True
        while q:
            node = q.popleft()
            for nei, w in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    par[nei][0] = node
                    sum_up[nei][0] = w
                    depth[nei] = depth[node] + 1
                    dist[nei] = dist[node] + w
                    q.append(nei)
        for k in range(1, LOG):
            for i in range(n):
                p = par[i][k - 1]
                if p != -1:
                    par[i][k] = par[p][k - 1]
                    sum_up[i][k] = sum_up[i][k - 1] + sum_up[p][k - 1]
        def get_lca(u: int, v: int) -> int:
            if depth[u] > depth[v]:
                u, v = v, u
            diff = depth[v] - depth[u]
            for k in range(LOG):
                if diff & (1 << k):
                    v = par[v][k]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if par[u][k] != -1 and par[v][k] != -1 and par[u][k] != par[v][k]:
                    u = par[u][k]
                    v = par[v][k]
            return par[u][0]
        ans = []
        for qu, qv in queries:
            if qu == qv:
                ans.append(qu)
                continue
            l = get_lca(qu, qv)
            total = dist[qu] + dist[qv] - 2 * dist[l]
            threshold = (total + 1) // 2
            du = dist[qu] - dist[l]
            if du >= threshold:
                cur = qu
                pref = 0
                for k in range(LOG - 1, -1, -1):
                    anc = par[cur][k]
                    if anc != -1 and depth[anc] >= depth[l] and pref + sum_up[cur][k] < threshold:
                        pref += sum_up[cur][k]
                        cur = anc
                med = par[cur][0]
            else:
                target_d = dist[l] + threshold - du
                cur = qv
                for k in range(LOG - 1, -1, -1):
                    anc = par[cur][k]
                    if anc != -1 and depth[anc] >= depth[l] and dist[anc] >= target_d:
                        cur = anc
                med = cur
            ans.append(med)
        return ans
# @lc code=end