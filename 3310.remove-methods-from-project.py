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
        # Build adjacency list
        g = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)

        # Step 1: find all suspicious methods reachable from k
        suspicious = [False] * n
        dq = deque([k])
        suspicious[k] = True
        while dq:
            u = dq.pop()
            for v in g[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    dq.append(v)

        # Step 2: check if any edge enters suspicious set from outside
        for a, b in invocations:
            if (not suspicious[a]) and suspicious[b]:
                return list(range(n))

        # Step 3: remove all suspicious methods
        return [i for i in range(n) if not suspicious[i]]
# @lc code=end
