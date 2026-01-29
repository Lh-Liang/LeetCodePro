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
        
        # Step 2: Find all suspicious methods using BFS starting from k
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)
        
        # Step 3: Check for external invocations
        # A group is removable only if no non-suspicious method invokes a suspicious one
        is_removable = True
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                is_removable = False
                break
        
        # Step 4: Return result based on the check
        if is_removable:
            return [i for i in range(n) if not suspicious[i]]
        else:
            # If not removable, return all original methods
            return list(range(n))
# @lc code=end