#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
from typing import List
from collections import deque, defaultdict

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency lists efficiently using sorting and sliding window
        idxs = list(range(n))
        idxs.sort(key=lambda i: nums[i])
        adj = [[] for _ in range(n)]
        # Use sliding window to connect nodes with |nums[i] - nums[j]| <= maxDiff
        j = 0
        for i in range(n):
            while j < n and nums[idxs[j]] - nums[idxs[i]] <= maxDiff:
                j += 1
            for k in range(i+1, j):
                u, v = idxs[i], idxs[k]
                if abs(nums[u] - nums[v]) <= maxDiff:
                    adj[u].append(v)
                    adj[v].append(u)
        # Step 2: For each query, do BFS from ui to vi (could be batched, but let's use on-demand BFS for each query)
        def bfs(u, v):
            if u == v:
                return 0
            visited = [False] * n
            visited[u] = True
            dq = deque([(u, 0)])
            while dq:
                curr, dist = dq.popleft()
                for nei in adj[curr]:
                    if not visited[nei]:
                        if nei == v:
                            return dist + 1
                        visited[nei] = True
                        dq.append((nei, dist + 1))
            return -1
        # Optionally, precompute connected components to quickly answer -1 for disconnected pairs
        comp = [-1] * n
        cid = 0
        for i in range(n):
            if comp[i] == -1:
                dq = deque([i])
                comp[i] = cid
                while dq:
                    curr = dq.popleft()
                    for nei in adj[curr]:
                        if comp[nei] == -1:
                            comp[nei] = cid
                            dq.append(nei)
                cid += 1
        res = []
        for u, v in queries:
            if comp[u] != comp[v]:
                res.append(-1)
            elif u == v:
                res.append(0)
            else:
                res.append(bfs(u, v))
        return res
# @lc code=end