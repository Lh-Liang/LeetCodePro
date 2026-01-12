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
        
        # Use iterative approach to get post-order traversal sequence
        order = []
        parent = [-1] * n
        stack = [0]
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
        
        dp0 = [0] * n
        dp1 = [0] * n
        
        # Process nodes in reverse pre-order (post-order traversal)
        for u in reversed(order):
            total_sum = 0
            gains = []
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                
                # Subtree at v is already processed
                total_sum += dp0[v]
                
                # Calculate potential gain if we keep edge (u, v)
                # dp1[v] + w is the sum if edge is kept, dp0[v] if removed
                gain = (dp1[v] + w) - dp0[v]
                if gain > 0:
                    gains.append(gain)
            
            gains.sort(reverse=True)
            
            # dp0[u]: Max sum if u can have k edges to children
            dp0[u] = total_sum + sum(gains[:k])
            
            # dp1[u]: Max sum if u can have k-1 edges to children (leaving 1 for parent)
            dp1[u] = total_sum + sum(gains[:k-1])
            
        return dp0[0]
# @lc code=end