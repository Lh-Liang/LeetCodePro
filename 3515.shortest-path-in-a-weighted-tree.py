#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        # Build adjacency list and edge mapping
        tree = defaultdict(list)
        edge_id = {}
        for i, (u, v, w) in enumerate(edges):
            tree[u].append((v, w, i))
            tree[v].append((u, w, i))
            edge_id[(u, v)] = i
            edge_id[(v, u)] = i

        # Euler Tour to flatten tree
        in_time = [0] * (n+1)
        out_time = [0] * (n+1)
        time = 1
        parent = [0] * (n+1)
        edge_to_parent = [0] * (n+1)
        def dfs(u, p, cumw):
            nonlocal time
            in_time[u] = time
            time += 1
            for v, w, idx in tree[u]:
                if v == p: continue
                parent[v] = u
                edge_to_parent[v] = w
                dfs(v, u, cumw + w)
            out_time[u] = time - 1
        dfs(1, 0, 0)

        # Fenwick Tree for path sum updates
        class BIT:
            def __init__(self, size):
                self.N = size + 2
                self.bit = [0] * (self.N)
            def add(self, i, x):
                while i < self.N:
                    self.bit[i] += x
                    i += i & -i
            def range_add(self, l, r, x):
                self.add(l, x)
                self.add(r+1, -x)
            def query(self, i):
                res = 0
                while i > 0:
                    res += self.bit[i]
                    i -= i & -i
                return res

        bit = BIT(n+2)
        # Initialize the path sums
        for u in range(2, n+1):
            bit.range_add(in_time[u], in_time[u], edge_to_parent[u])

        # For edge updates, keep track of edge weights
        edge_weight = {}
        for i, (u, v, w) in enumerate(edges):
            edge_weight[i] = w

        res = []
        for q in queries:
            if q[0] == 1:
                _, u, v, w_new = q
                # Find which node is deeper
                if parent[u] == v:
                    child = u
                else:
                    child = v
                idx = edge_id[(u, v)]
                diff = w_new - edge_weight[idx]
                edge_weight[idx] = w_new
                # update subtree rooted at child
                bit.range_add(in_time[child], out_time[child], diff)
            else:
                _, x = q
                res.append(bit.query(in_time[x]))
        return res
# @lc code=end