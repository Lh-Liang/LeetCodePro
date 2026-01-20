#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)
        
        # Compute suspicious set S: reachable from k
        susp = set()
        q = deque([k])
        susp.add(k)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in susp:
                    susp.add(v)
                    q.append(v)
        
        # Check if removable: no incoming edges from outside to S
        can_remove = True
        for a, b in invocations:
            if a not in susp and b in susp:
                can_remove = False
                break
        
        if can_remove:
            return [i for i in range(n) if i not in susp]
        else:
            return list(range(n))
        
# @lc code=end
