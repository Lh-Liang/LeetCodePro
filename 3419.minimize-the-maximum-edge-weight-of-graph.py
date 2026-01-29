#
# @lc app=leetcode id=3419 lang=python3
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
import collections
from typing import List

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # The core insight is that if node 0 can reach all nodes in the reversed graph,
        # we can always extract a spanning tree where each node has out-degree 1.
        # Since threshold >= 1, the out-degree constraint is satisfied by any valid reachability.
        
        # Build reversed adjacency list: v -> u
        adj = collections.defaultdict(list)
        unique_weights = set()
        for u, v, w in edges:
            adj[v].append((u, w))
            unique_weights.add(w)
        
        sorted_weights = sorted(list(unique_weights))
        
        def can_reach_all(limit: int) -> bool:
            visited = [False] * n
            visited[0] = True
            queue = collections.deque([0])
            count = 1
            
            while queue:
                curr = queue.popleft()
                for neighbor, weight in adj[curr]:
                    if not visited[neighbor] and weight <= limit:
                        visited[neighbor] = True
                        count += 1
                        if count == n:
                            return True
                        queue.append(neighbor)
            return count == n

        # Binary search on the sorted unique weights
        low = 0
        high = len(sorted_weights) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach_all(sorted_weights[mid]):
                ans = sorted_weights[mid]
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
# @lc code=end