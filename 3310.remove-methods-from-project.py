#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)
        
        visited = [False] * n
        S = set()
        stack = [k]
        visited[k] = True
        while stack:
            u = stack.pop()
            S.add(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        
        can_remove = True
        for a, b in invocations:
            if a not in S and b in S:
                can_remove = False
                break
        
        if not can_remove:
            return list(range(n))
        
        return [i for i in range(n) if i not in S]

# @lc code=end