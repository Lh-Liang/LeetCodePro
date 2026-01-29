#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # BFS to get post-order traversal and parent pointers
        order = []
        parent = [-1] * n
        parent_w = [0] * n
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        
        while queue:
            u = queue.popleft()
            order.append(u)
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    parent_w[v] = w
                    queue.append(v)
        
        # f[u][0]: max weight in subtree u, u can have k edges to children (no parent edge)
        # f[u][1]: max weight in subtree u, u can have k-1 edges to children (parent edge kept)
        f = [[0, 0] for _ in range(n)]
        
        # Process nodes in reverse order (bottom-up)
        for u in reversed(order):
            base_sum = 0
            diffs = []
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                
                # Default: don't keep edge (u, v)
                base_sum += f[v][0]
                # Gain if we keep edge (u, v)
                d = f[v][1] + w - f[v][0]
                if d > 0:
                    diffs.append(d)
            
            diffs.sort(reverse=True)
            
            # f[u][0] allows up to k edges to children
            f[u][0] = base_sum + sum(diffs[:k])
            # f[u][1] allows up to k-1 edges to children
            f[u][1] = base_sum + sum(diffs[:k-1])
            
        return f[0][0]
# @lc code=end