#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        # Build adjacency list
        adj = [[] for _ in range(n)]
        sets = [set(prop) for prop in properties]
        for i in range(n):
            for j in range(i+1, n):
                if len(sets[i] & sets[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        # Count connected components using DFS
        visited = [False] * n
        def dfs(u):
            stack = [u]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for v in adj[node]:
                        if not visited[v]:
                            stack.append(v)
        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)
        return components
# @lc code=end