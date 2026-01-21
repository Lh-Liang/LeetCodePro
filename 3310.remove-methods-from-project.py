from collections import deque
from typing import List

#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list for the graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
        
        # Step 2: Find all suspicious methods using BFS starting from method k
        # A method is suspicious if it is k or reachable from k
        is_suspicious = [False] * n
        is_suspicious[k] = True
        queue = deque([k])
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not is_suspicious[v]:
                    is_suspicious[v] = True
                    queue.append(v)
        
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        # The suspicious methods can only be removed if no such edge exists
        can_remove = True
        for u, v in invocations:
            if not is_suspicious[u] and is_suspicious[v]:
                can_remove = False
                break
        
        # Step 4: Determine the result based on the removal condition
        if not can_remove:
            # If cannot remove, return all methods
            return list(range(n))
        
        # If can remove, return only the non-suspicious methods
        return [i for i in range(n) if not is_suspicious[i]]
# @lc code=end