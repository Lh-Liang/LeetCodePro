#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        parent = [0] * (n + 1)
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        edge_weight_at_node = [0] * (n + 1)
        
        # Iterative DFS to compute tin, tout, and parent-child mapping
        timer = 0
        stack = [(1, iter(adj[1]))]
        timer += 1
        tin[1] = timer
        
        while stack:
            u, children = stack[-1]
            try:
                v, w = next(children)
                if v != parent[u]:
                    parent[v] = u
                    edge_weight_at_node[v] = w
                    timer += 1
                    tin[v] = timer
                    stack.append((v, iter(adj[v])))
            except StopIteration:
                tout[u] = timer
                stack.pop()
        
        # Binary Indexed Tree for range updates (difference array approach)
        bit = [0] * (n + 2)
        def bit_update(i, delta):
            while i < n + 2:
                bit[i] += delta
                i += i & (-i)
        
        def bit_query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        
        # Initial edge weights as range updates in the BIT
        for v in range(2, n + 1):
            w = edge_weight_at_node[v]
            bit_update(tin[v], w)
            bit_update(tout[v] + 1, -w)
        
        results = []
        for q in queries:
            if q[0] == 1:
                u, v, w_new = q[1], q[2], q[3]
                # Identify which node is the child in the edge (u, v)
                child = v if parent[v] == u else u
                old_w = edge_weight_at_node[child]
                delta = w_new - old_w
                # Update the distance for all nodes in the child's subtree
                bit_update(tin[child], delta)
                bit_update(tout[child] + 1, -delta)
                edge_weight_at_node[child] = w_new
            else:
                x = q[1]
                # Distance from root to x is the prefix sum of the difference array
                results.append(bit_query(tin[x]))
        
        return results
# @lc code=end