#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        import collections
        MOD = 10**9 + 7
        n = len(edges) + 1
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Precompute depths and parents for LCA computation
        depth = [-1] * (n + 1)
        parent = [-1] * (n + 1)
        
        def dfs(node, par, dep):
            depth[node] = dep
            parent[node] = par
            for neighbor in graph[node]:
                if neighbor == par:
                    continue
                dfs(neighbor, node, dep + 1)
        
        dfs(1, -1, 0) # Root at node 1 with depth 0
        
        def lca(u, v):
            if depth[u] < depth[v]: # Ensure u is deeper than v or same level.
                u, v = v, u 
            # Bring u to the same depth as v. 
            while depth[u] > depth[v]: 
                u = parent[u]
            # Now bring both to their common ancestor. 
            while u != v:
                u = parent[u]
                v = parent[v]
            return u 
         
         def path_length(u, v): 
             lca_node = lca(u, v) 
             return depth[u] + depth[v] - 2 * depth[lca_node] 
         result = [] 
         for ui, vi in queries: 
             length = path_length(ui, vi) 
             if length == 0: 
                 result.append(0) # No edges in path from node to itself. 
             else: # There are length ways to assign weights such that cost is odd. 
                 result.append(pow(2, length - 1, MOD)) # Either choose an odd number of '1' or '2'. 
         return result # @lc code=end