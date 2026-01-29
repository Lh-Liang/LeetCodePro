#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0
        def manhattan(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        def check(D: int) -> bool:
            graph = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if manhattan(points[i], points[j]) < D:
                        graph[i].append(j)
                        graph[j].append(i)
            color = [-1] * n
            from collections import deque
            for start in range(n):
                if color[start] == -1:
                    q = deque([start])
                    color[start] = 0
                    while q:
                        u = q.popleft()
                        for v in graph[u]:
                            if color[v] == -1:
                                color[v] = 1 - color[u]
                                q.append(v)
                            elif color[v] == color[u]:
                                return False
            return True
        l, r = 0, 400000010
        while l < r:
            mid = l + (r - l + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

# @lc code=end