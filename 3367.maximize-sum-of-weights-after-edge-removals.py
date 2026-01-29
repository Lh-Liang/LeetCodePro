#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # Iterative DFS to get post-order traversal to avoid recursion limits
        order = []
        stack = [0]
        parent = [-1] * n
        visited = [False] * n
        visited[0] = True
        
        while stack:
            u = stack.pop()
            order.append(u)
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        
        # dp0[u]: max sum in subtree u if edge (parent, u) is NOT kept
        # dp1[u]: max sum in subtree u if edge (parent, u) IS kept
        dp0 = [0] * n
        dp1 = [0] * n
        
        for u in reversed(order):
            base_sum = 0
            diffs = []
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                
                base_sum += dp0[v]
                # Profit of picking the edge to child v
                diff = w + dp1[v] - dp0[v]
                if diff > 0:
                    diffs.append(diff)
            
            diffs.sort(reverse=True)
            
            # For dp0, we can pick up to k edges to children
            dp0[u] = base_sum + sum(diffs[:k])
            
            # For dp1, we can pick up to k-1 edges to children (one slot reserved for parent)
            dp1[u] = base_sum + sum(diffs[:k-1])
            
        return dp0[0]
# @lc code=end