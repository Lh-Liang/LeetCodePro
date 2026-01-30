#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list efficiently
        idx = sorted(range(n), key=lambda x: nums[x])
        adj = [[] for _ in range(n)]
        l = 0
        for r in range(n):
            while nums[idx[r]] - nums[idx[l]] > maxDiff:
                l += 1
            for k in range(l, r):
                adj[idx[r]].append(idx[k])
                adj[idx[k]].append(idx[r])
        # Step 2: Preprocess connected components using BFS
        comp_id = [-1] * n
        cid = 0
        for node in range(n):
            if comp_id[node] == -1:
                dq = deque([node])
                comp_id[node] = cid
                while dq:
                    curr = dq.popleft()
                    for nei in adj[curr]:
                        if comp_id[nei] == -1:
                            comp_id[nei] = cid
                            dq.append(nei)
                cid += 1
        # Step 3: For same-component queries, use BFS from source if needed
        q_by_src = defaultdict(list)
        for i, (u, v) in enumerate(queries):
            q_by_src[u].append((v, i))
        res = [-1] * len(queries)
        for u in q_by_src:
            # Group queries by connected component
            rel_queries = [ (v, idxq) for v, idxq in q_by_src[u] if comp_id[u] == comp_id[v] ]
            unreachable_queries = [ (v, idxq) for v, idxq in q_by_src[u] if comp_id[u] != comp_id[v] ]
            # For unreachable, set -1
            for v, idxq in unreachable_queries:
                res[idxq] = -1
            if rel_queries:
                visited = [-1] * n
                dq = deque()
                dq.append(u)
                visited[u] = 0
                while dq:
                    node = dq.popleft()
                    for nei in adj[node]:
                        if visited[nei] == -1:
                            visited[nei] = visited[node] + 1
                            dq.append(nei)
                for v, idxq in rel_queries:
                    if u == v:
                        res[idxq] = 0
                    else:
                        res[idxq] = visited[v]
        return res
# @lc code=end