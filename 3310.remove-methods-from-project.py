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
        # Step 1: Build the adjacency list for reachability
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
        
        # Step 2: Find all suspicious methods using BFS
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    queue.append(v)
        
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        # A group can only be removed if no method OUTSIDE invokes a method WITHIN.
        can_remove = True
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                can_remove = False
                break
        
        # Step 4: Return the result based on the validation
        if not can_remove:
            return list(range(n))
        
        return [i for i in range(n) if not suspicious[i]]
# @lc code=end