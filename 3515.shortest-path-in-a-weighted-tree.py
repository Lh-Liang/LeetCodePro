#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
import sys

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        parent_edge_weight = [0] * (n + 1)
        child_node_map = {}
        
        # Iterative DFS to linearize the tree and map edges to child nodes
        timer = 0
        stack = [(1, -1)]
        adj_iter = [iter(adj[i]) for i in range(n + 1)]
        
        timer += 1
        tin[1] = timer
        
        while stack:
            u, p = stack[-1]
            try:
                v, w = next(adj_iter[u])
                if v != p:
                    timer += 1
                    tin[v] = timer
                    parent_edge_weight[v] = w
                    # Map edge to the child node
                    edge_key = (u, v) if u < v else (v, u)
                    child_node_map[edge_key] = v
                    stack.append((v, u))
            except StopIteration:
                tout[u] = timer
                stack.pop()

        # BIT for Range Update (tin[v] to tout[v]) and Point Query (tin[x])
        # We use a difference array approach: update(L, delta), update(R+1, -delta)
        bit = [0] * (n + 2)

        def bit_update(i, delta):
            while i <= n + 1:
                bit[i] += delta
                i += i & (-i)

        def bit_query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        # Initialize BIT with starting weights
        for i in range(2, n + 1):
            w = parent_edge_weight[i]
            bit_update(tin[i], w)
            bit_update(tout[i] + 1, -w)

        results = []
        for q in queries:
            if q[0] == 1:
                u, v, w_new = q[1], q[2], q[3]
                edge_key = (u, v) if u < v else (v, u)
                c = child_node_map[edge_key]
                delta = w_new - parent_edge_weight[c]
                parent_edge_weight[c] = w_new
                # Range update on subtree of child c
                bit_update(tin[c], delta)
                bit_update(tout[c] + 1, -delta)
            else:
                x = q[1]
                # Point query: prefix sum in BIT gives path distance
                results.append(bit_query(tin[x]))

        return results
# @lc code=end