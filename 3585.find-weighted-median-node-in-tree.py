#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
from typing import List
import sys
sys.setrecursionlimit(1 << 20)

class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        import math
        LOG = max(1, (n-1).bit_length())
        tree = [[] for _ in range(n)]
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))
        up = [[-1]*LOG for _ in range(n)]
        depth = [0]*n
        dist = [0]*n
        def dfs(u, p):
            up[u][0] = p
            for k in range(1, LOG):
                if up[u][k-1] != -1:
                    up[u][k] = up[up[u][k-1]][k-1]
            for v, w in tree[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    dfs(v, u)
        dfs(0, -1)
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in reversed(range(LOG)):
                if up[u][k] != -1 and depth[up[u][k]] >= depth[v]:
                    u = up[u][k]
            if u == v:
                return u
            for k in reversed(range(LOG)):
                if up[u][k] != -1 and up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return up[u][0]
        def jump(u, steps):
            for k in range(LOG):
                if steps & (1<<k):
                    u = up[u][k]
            return u
        res = []
        for u, v in queries:
            lca = get_lca(u, v)
            total = dist[u] + dist[v] - 2*dist[lca]
            half = total / 2
            # Walk from u to v, keep sum from u, stop at first node >= half
            # We can walk up from u to lca, then down from lca to v
            path = []
            # u to lca
            node = u
            su = 0
            steps_up = depth[u] - depth[lca]
            node_u = u
            for k in reversed(range(LOG)):
                while steps_up >= (1<<k):
                    node_u = up[node_u][k]
                    steps_up -= (1<<k)
            # Down path from lca to v
            down_path = []
            node_v = v
            par = up
            trace = []
            while node_v != lca:
                trace.append(node_v)
                node_v = up[node_v][0]
            trace.reverse()
            path_nodes = []
            # u to lca (including u)
            node_u2 = u
            path_nodes.append(node_u2)
            while node_u2 != lca:
                node_u2 = up[node_u2][0]
                path_nodes.append(node_u2)
            # lca to v (excluding lca)
            node_v2 = v
            down_nodes = []
            while node_v2 != lca:
                down_nodes.append(node_v2)
                node_v2 = up[node_v2][0]
            down_nodes = down_nodes[::-1]
            path_nodes += down_nodes
            # Now path_nodes is the node list from u to v
            # Get edge weights along the path
            # For each step, get the edge weight from previous node to current
            weights = []
            for i in range(1, len(path_nodes)):
                a, b = path_nodes[i-1], path_nodes[i]
                for nxt, w in tree[a]:
                    if nxt == b:
                        weights.append(w)
                        break
            # Now, step through the path to find the first node whose sum from u >= half
            curr_sum = 0
            idx = 0
            found = False
            for i in range(1, len(path_nodes)):
                curr_sum += weights[i-1]
                if curr_sum >= half:
                    res.append(path_nodes[i])
                    found = True
                    break
            if not found:
                res.append(path_nodes[-1])
        return res
# @lc code=end