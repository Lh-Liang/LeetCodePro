#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
        
        suspicious = [False] * n
        suspicious[k] = True
        stack = [k]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    stack.append(v)
        
        can_remove = True
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                can_remove = False
                break
        
        if can_remove:
            return [i for i in range(n) if not suspicious[i]]
        else:
            return list(range(n))
# @lc code=end