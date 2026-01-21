#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
from typing import List
import collections

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # Reverse graph: node 0 must be reachable from all other nodes
        # is equivalent to node 0 reaching all other nodes in the reversed graph.
        adj = collections.defaultdict(list)
        max_w = 0
        for u, v, w in edges:
            # Original: u -> v. Reversed: v -> u.
            adj[v].append((u, w))
            if w > max_w:
                max_w = w
        
        def check(limit):
            visited = [False] * n
            visited[0] = True
            queue = collections.deque([0])
            count = 1
            
            while queue:
                u = queue.popleft()
                for v, w in adj[u]:
                    if w <= limit and not visited[v]:
                        visited[v] = True
                        count += 1
                        queue.append(v)
            
            return count == n

        low = 1
        high = max_w
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
# @lc code=end