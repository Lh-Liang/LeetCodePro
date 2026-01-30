#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(1 << 20)

        # Build adjacency list and edge mapping
        tree = defaultdict(list)
        edge_map = {}
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))
            edge_map[frozenset((u,v))] = w

        # DFS to assign parent, depth, subtree range
        tin = [0] * (n+1)
        tout = [0] * (n+1)
        parent = [0] * (n+1)
        edge_to_parent = [0] * (n+1)
        depth = [0] * (n+1)
        time = 0
        def dfs(u, p, d):
            nonlocal time
            time += 1
            tin[u] = time
            for v, w in tree[u]:
                if v != p:
                    parent[v] = u
                    edge_to_parent[v] = w
                    depth[v] = d + w
                    dfs(v, u, d + w)
            tout[u] = time
        dfs(1, 0, 0)

        # BIT for range update and query
        class BIT:
            def __init__(self, n):
                self.n = n+2
                self.tree = [0]*(self.n+2)
            def update(self, i, x):
                while i < self.n:
                    self.tree[i] += x
                    i += i&-i
            def query(self, i):
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i&-i
                return res
            def range_add(self, l, r, x):
                self.update(l, x)
                self.update(r+1, -x)
        bit = BIT(n+2)
        res = []
        for q in queries:
            if q[0] == 1:
                _, u, v, w_new = q
                key = frozenset((u, v))
                # Find child in (u, v)
                if parent[u] == v:
                    child = u
                else:
                    child = v
                old_w = edge_to_parent[child]
                diff = w_new - old_w
                edge_to_parent[child] = w_new
                # Range add to all subtree of child
                bit.range_add(tin[child], tout[child], diff)
            else:
                _, x = q
                ans = depth[x] + bit.query(tin[x])
                res.append(ans)
        return res
# @lc code=end