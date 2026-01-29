#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list for the directed graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
        
        # Step 2: Use BFS to identify all suspicious methods (reachable from k)
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)
        
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        # This ensures the 'suspicious group' is isolated from the rest of the project
        can_remove = True
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                can_remove = False
                break
        
        # Step 4: Return result based on the removal condition
        if can_remove:
            return [i for i in range(n) if not suspicious[i]]
        else:
            return list(range(n))
# @lc code=end