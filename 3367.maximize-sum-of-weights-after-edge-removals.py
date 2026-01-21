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
        
        # Standard iterative post-order traversal for tree DP
        parent = [-1] * n
        order = []
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
        
        f0 = [0] * n
        f1 = [0] * n
        
        for u in reversed(order):
            base_sum = 0
            diffs = []
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                base_sum += f0[v]
                d = f1[v] + w - f0[v]
                if d > 0:
                    diffs.append(d)
            
            diffs.sort(reverse=True)
            
            # f0[u]: max k edges to children (parent edge not kept)
            # f1[u]: max k-1 edges to children (parent edge kept)
            
            # Calculate f1[u] first (up to k-1 neighbors)
            gain_k_minus_1 = sum(diffs[:k-1])
            f1[u] = base_sum + gain_k_minus_1
            
            # Calculate f0[u] (up to k neighbors)
            if len(diffs) >= k:
                f0[u] = f1[u] + diffs[k-1]
            else:
                f0[u] = f1[u] + (diffs[len(diffs)-1] if len(diffs) > k-1 else 0)
            # Re-calculating cleanly for safety
            f0[u] = base_sum + sum(diffs[:k])
            
        return f0[0]
# @lc code=end