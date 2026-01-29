#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
import collections

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Iterative Tree Traversal to avoid recursion limits
        parent = [-1] * n
        order = []
        queue = collections.deque([0])
        visited = [False] * n
        visited[0] = True
        
        while queue:
            u = queue.popleft()
            order.append(u)
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        
        # dp0[u]: max sum for subtree u if u can have k edges to children
        # dp1[u]: max sum for subtree u if u can have k-1 edges to children
        dp0 = [0] * n
        dp1 = [0] * n
        
        # Process nodes from leaves to root
        for u in reversed(order):
            base_total = 0
            gains = []
            
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                
                # Option A: Don't keep edge (u, v)
                base_total += dp0[v]
                
                # Option B: Keep edge (u, v). Gain is (w + dp1[v]) - dp0[v]
                gain = w + dp1[v] - dp0[v]
                if gain > 0:
                    gains.append(gain)
            
            gains.sort(reverse=True)
            
            # Calculate DP states by picking best positive gains
            sum_gains = sum(gains)
            num_gains = len(gains)
            
            # For dp0, we can take up to k gains
            if num_gains <= k:
                dp0[u] = base_total + sum_gains
            else:
                dp0[u] = base_total + sum(gains[:k])
                
            # For dp1, we can take up to k-1 gains
            if num_gains <= k - 1:
                dp1[u] = base_total + sum_gains
            else:
                dp1[u] = base_total + sum(gains[:k-1])
        
        return dp0[0]
# @lc code=end