#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#

from typing import List

# @lc code=start
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        def get_dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        def can_partition(T: int) -> bool:
            n = len(points)
            adj = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if get_dist(i, j) < T:
                        adj[i].append(j)
                        adj[j].append(i)
            color = [-1] * n
            
            def bfs(start: int) -> bool:
                from collections import deque
                q = deque([start])
                color[start] = 0
                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            q.append(v)
                        elif color[v] == color[u]:
                            return False
                return True
            
            for i in range(n):
                if color[i] == -1:
                    if not bfs(i):
                        return False
            # Graph is bipartite
            if n == 2:
                return T <= 0
            return True
        
        low, high = 0, 2 * 10**9
        while low < high:
            mid = (low + high + 1) // 2
            if can_partition(mid):
                low = mid
            else:
                high = mid - 1
        return low
# @lc code=end
