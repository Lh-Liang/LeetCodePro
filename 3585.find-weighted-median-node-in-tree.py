#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def findMedian(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        LOG = 18
        up = [[-1] * LOG for _ in range(n)]
        dist = [0] * n
        depth = [0] * n
        
        # Standard BFS to precompute depth, dist and first parent
        stack = [(0, -1, 0, 0)]
        while stack:
            u, p, d, w_sum = stack.pop()
            up[u][0] = p
            depth[u] = d
            dist[u] = w_sum
            for v, w in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1, w_sum + w))
        
        # Binary lifting table
        for j in range(1, LOG):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        ans = []
        for u, v in queries:
            lca = get_lca(u, v)
            total_weight = dist[u] + dist[v] - 2 * dist[lca]
            
            # Weight from u to LCA
            u_to_lca_weight = dist[u] - dist[lca]
            
            # Check if median is on u -> LCA segment
            # Condition: 2 * weight(u, x) >= total_weight
            if 2 * u_to_lca_weight >= total_weight:
                # Find the first node x on path u -> LCA s.t. 2*(dist[u] - dist[x]) >= total_weight
                # This is the lowest ancestor x s.t. dist[x] <= dist[u] - total_weight / 2
                curr = u
                # We jump up as much as possible while the condition '2*(dist[u] - dist[anc]) < total_weight' is true
                for j in range(LOG - 1, -1, -1):
                    anc = up[curr][j]
                    if anc != -1 and depth[anc] >= depth[lca]:
                        if 2 * (dist[u] - dist[anc]) < total_weight:
                            curr = anc
                # After moving as high as possible without crossing the threshold,
                # the 'first' node to cross it is the parent of curr.
                # If u itself satisfies it (which happens if total_weight=0), the loop does nothing.
                if 2 * (dist[u] - dist[curr]) >= total_weight:
                    ans.append(curr)
                else:
                    ans.append(up[curr][0])
            else:
                # Median is on LCA -> v segment
                # Find the first node x on path LCA -> v s.t. 2*(u_to_lca_weight + dist[x] - dist[lca]) >= total_weight
                # This is the highest ancestor x of v s.t. 2*(dist[u] + dist[x] - 2*dist[lca]) >= total_weight
                curr = v
                # We jump up as much as possible while the condition '2*(dist[u] + dist[anc] - 2*dist[lca]) >= total_weight' is true
                for j in range(LOG - 1, -1, -1):
                    anc = up[curr][j]
                    if anc != -1 and depth[anc] >= depth[lca]:
                        if 2 * (dist[u] + dist[anc] - 2 * dist[lca]) >= total_weight:
                            curr = anc
                ans.append(curr)
                
        return ans
# @lc code=end