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
        # Helper to compute Manhattan distance
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # List all pairwise distances
        distances = []
        for i in range(n):
            for j in range(i+1, n):
                distances.append(manhattan(points[i], points[j]))
        distances = sorted(set(distances))

        # Check if it's possible to split points into two groups (non-empty) such that all intra-group manhattan distances >= d
        from collections import deque
        def can_partition(d):
            # Build graph: edge between points if distance < d (they can't be in same group)
            graph = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i+1, n):
                    if manhattan(points[i], points[j]) < d:
                        graph[i].append(j)
                        graph[j].append(i)
            # Try to 2-color the graph
            color = [None] * n
            for start in range(n):
                if color[start] is not None:
                    continue
                queue = deque([start])
                color[start] = 0
                while queue:
                    u = queue.popleft()
                    for v in graph[u]:
                        if color[v] is None:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False  # Not bipartite
            return True

        # Binary search on distances
        left, right = 0, len(distances)-1
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            d = distances[mid]
            if can_partition(d):
                answer = d
                left = mid + 1
            else:
                right = mid - 1
        return answer
# @lc code=end