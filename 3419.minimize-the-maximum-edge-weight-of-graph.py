#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Node 0 must be reachable from all other nodes.
        # In the reversed graph, node 0 must reach all other nodes.
        # The constraint 'threshold >= 1' ensures that if reachability is possible,
        # we can always satisfy the outgoing edge limit by keeping only one edge per node (spanning tree).
        
        # Build reversed adjacency list: v -> u with weight w
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[v].append((u, w))
        
        # Extract and sort unique weights for binary search
        weights = sorted(list(set(e[2] for e in edges)))
        
        # Helper function to check if node 0 can reach all nodes in reversed graph
        # using only edges with weight <= max_w
        def check(max_w):
            visited = [False] * n
            visited[0] = True
            q = deque([0])
            count = 1
            
            while q:
                u = q.popleft()
                for v, w in adj[u]:
                    if w <= max_w and not visited[v]:
                        visited[v] = True
                        count += 1
                        if count == n:
                            return True
                        q.append(v)
            return count == n
        
        # Binary search over the sorted unique weights
        low, high = 0, len(weights) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(weights[mid]):
                ans = weights[mid]
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
# @lc code=end