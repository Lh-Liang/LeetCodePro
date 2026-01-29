#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # Helper function to perform BFS and return distance mapping
        def bfs(tree_edges, n):
            adj = defaultdict(list)
            for u, v in tree_edges:
                adj[u].append(v)
                adj[v].append(u)
            dist = [[-1] * n for _ in range(n)]
            for start in range(n):
                queue = deque([start])
                dist[start][start] = 0
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if dist[start][neighbor] == -1:
                            dist[start][neighbor] = dist[start][node] + 1
                            queue.append(neighbor)
            return dist
        
        # Get distances for both trees using BFS
        n, m = len(edges1) + 1, len(edges2) + 1
        distance1 = bfs(edges1, n)
        distance2 = bfs(edges2, m)
        
        # Calculate max target nodes for each node in first tree by connecting it to all nodes in second tree
        result = []
        for i in range(n):
            max_targets = 0
            for j in range(m):
                current_targets = sum(
distance1[i][k] % 2 == (distance1[i][k] + distance2[j][l]) % 2 \
in range(n) for l in range(m))
                max_targets = max(max_targets, current_targets)
            result.append(max_targets)
        
        return result