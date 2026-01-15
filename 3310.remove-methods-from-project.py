#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build adjacency list for forward edges (who invokes whom)
        adj = [[] for _ in range(n)]
        # Also build reverse adjacency list (who is invoked by whom) to check incoming edges from outside suspicious group
        reverse_adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)
            reverse_adj[b].append(a)
        
        # Step 1: Find all suspicious methods (reachable from k via DFS/BFS)
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    stack.append(neighbor)
        
        # Step 2: Check if any method outside the suspicious group invokes a method inside the suspicious group.
        # That is, for any invocation (a,b) where a not suspicious and b suspicious, we cannot remove.
        can_remove = True
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                can_remove = False
                break
        
        if not can_remove:
            return list(range(n))
        
        # Step 3: Return all methods that are not suspicious.
        return [i for i in range(n) if not suspicious[i]]
# @lc code=end