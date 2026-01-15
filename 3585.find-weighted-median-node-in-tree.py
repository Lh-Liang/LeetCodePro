#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#
# @lc code=start
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        LOG = 18
        parent = [[-1] * n for _ in range(LOG)]
        dist_to_root = [0] * n
        depth = [0] * n
        dist_up = [[0] * n for _ in range(LOG)]
        
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        while queue:
            node = queue.popleft()
            for neighbor, weight in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[0][neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    dist_to_root[neighbor] = dist_to_root[node] + weight
                    dist_up[0][neighbor] = weight
                    queue.append(neighbor)
        
        for k in range(1, LOG):
            for v in range(n):
                if parent[k-1][v] != -1:
                    mid = parent[k-1][v]
                    parent[k][v] = parent[k-1][mid]
                    dist_up[k][v] = dist_up[k-1][v] + dist_up[k-1][mid]
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]
        
        results = []
        for u, v in queries:
            if u == v:
                results.append(u)
                continue
            
            l = lca(u, v)
            total_weight = dist_to_root[u] + dist_to_root[v] - 2 * dist_to_root[l]
            cumulative_at_lca = dist_to_root[u] - dist_to_root[l]
            
            if 2 * cumulative_at_lca >= total_weight:
                curr = u
                cumulative = 0
                for k in range(LOG - 1, -1, -1):
                    anc = parent[k][curr]
                    if anc != -1 and depth[anc] >= depth[l]:
                        new_cumulative = cumulative + dist_up[k][curr]
                        if 2 * new_cumulative < total_weight:
                            curr = anc
                            cumulative = new_cumulative
                results.append(parent[0][curr])
            else:
                curr = v
                dist_from_v = 0
                for k in range(LOG - 1, -1, -1):
                    anc = parent[k][curr]
                    if anc != -1 and depth[anc] > depth[l]:
                        new_dist = dist_from_v + dist_up[k][curr]
                        cumulative_at_anc = cumulative_at_lca + (dist_to_root[v] - dist_to_root[l]) - new_dist
                        if 2 * cumulative_at_anc >= total_weight:
                            curr = anc
                            dist_from_v = new_dist
                results.append(curr)
        
        return results
# @lc code=end