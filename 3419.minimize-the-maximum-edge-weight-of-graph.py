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
        # Build reversed adjacency list: v -> u
        # Original: u -> v (u can reach v)
        # Reversed: v -> u (v can reach u)
        # If 0 can reach all nodes in reversed graph, all nodes can reach 0 in original.
        rev_adj = collections.defaultdict(list)
        max_weight = 0
        for u, v, w in edges:
            rev_adj[v].append((u, w))
            if w > max_weight:
                max_weight = w
        
        def check(limit: int) -> bool:
            # BFS to check if node 0 can reach all nodes using weights <= limit
            visited = [False] * n
            visited[0] = True
            queue = collections.deque([0])
            count = 1
            
            while queue:
                curr = queue.popleft()
                for neighbor, weight in rev_adj[curr]:
                    if not visited[neighbor] and weight <= limit:
                        visited[neighbor] = True
                        count += 1
                        if count == n:
                            return True
                        queue.append(neighbor)
            return count == n

        # Binary search on the weight range
        low = 1
        high = max_weight
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