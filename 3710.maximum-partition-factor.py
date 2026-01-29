#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#

# @lc code=start
from typing import List
import collections

class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0
        
        # Precompute all pairwise Manhattan distances
        dists_list = []
        adj_data = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dists_list.append(d)
                adj_data.append((i, j, d))
        
        # The candidate values for the maximum partition factor are the distances themselves
        unique_dists = sorted(list(set(dists_list)))
        
        def is_bipartite(threshold):
            # Build graph where edges are pairs with distance < threshold
            # If this graph is bipartite, we can achieve a partition factor >= threshold
            adj = [[] for _ in range(n)]
            for i, j, d in adj_data:
                if d < threshold:
                    adj[i].append(j)
                    adj[j].append(i)
            
            color = [-1] * n
            for i in range(n):
                if color[i] == -1:
                    color[i] = 0
                    queue = collections.deque([i])
                    while queue:
                        u = queue.popleft()
                        for v in adj[u]:
                            if color[v] == -1:
                                color[v] = 1 - color[u]
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False
            return True

        # Binary search for the maximum distance X such that G_X is bipartite
        low = 0
        high = len(unique_dists) - 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if is_bipartite(unique_dists[mid]):
                ans = unique_dists[mid]
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
# @lc code=end