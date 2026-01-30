#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        from collections import deque

        n = len(points)
        if n == 2:
            return 0

        # Precompute all unique pairwise Manhattan distances
        dists = set()
        for i in range(n):
            for j in range(i+1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dists.add(d)
        dists = sorted(list(dists))
        dists.append(10**18)  # Handle edge case where groups can be completely separated

        def is_bipartite(k):
            # Build graph: edge between (i, j) if dist < k
            adj = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i+1, n):
                    d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    if d < k:
                        adj[i].append(j)
                        adj[j].append(i)
            color = [0] * n
            for i in range(n):
                if color[i] == 0:
                    queue = deque([i])
                    color[i] = 1
                    while queue:
                        u = queue.popleft()
                        for v in adj[u]:
                            if color[v] == 0:
                                color[v] = -color[u]
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False
            # Verify both groups are non-empty
            color_count = sum(1 for c in color if c == 1)
            return 0 < color_count < n

        # Binary search for the maximal k
        left, right = 0, len(dists)-1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            k = dists[mid]
            if is_bipartite(k):
                ans = k
                left = mid + 1
            else:
                right = mid - 1
        return ans
# @lc code=end