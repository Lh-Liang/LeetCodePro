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
        sets = [set(p) for p in properties]
        for i in range(n):
            for j in range(i+1, n):
                if len(sets[i] & sets[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        # Count connected components using DFS
        visited = [False] * n
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count
# @lc code=end