#
# @lc app=leetcode id=3585 lang=python3
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        def dfs(u, v):
            if u == v:
                return [v], 0
            visited.add(u)
            for nei, weight in graph[u]:
                if nei not in visited:
                    path, w = dfs(nei, v)
                    if path:
                        return [u] + path, w + weight
            return [], 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        results = []
        for u, v in queries:
            visited = set()
            path, total_weight = dfs(u,v)
            half_weight = total_weight / 2.0
            current_weight = 0.0
            for i in range(len(path) - 1):
                current_node = path[i]
                next_node = path[i+1]
                current_weight += dict(graph[current_node])[next_node]'s weight = dict(graph[current_node])[next_node] 'if current_weight >= half_weight:'return current_node