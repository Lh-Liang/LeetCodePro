#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
import collections

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
        
        # Step 2: Find all suspicious methods using BFS
        suspicious = [False] * n
        suspicious[k] = True
        queue = collections.deque([k])
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    queue.append(v)
        
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        external_call_exists = False
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                external_call_exists = True
                break
        
        # Step 4: Return result based on the check
        if external_call_exists:
            return list(range(n))
        else:
            return [i for i in range(n) if not suspicious[i]]
# @lc code=end