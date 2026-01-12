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
        
        # Calculate all pairwise Manhattan distances
        dists = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dists.append(abs(x1 - x2) + abs(y1 - y2))
        
        # Sort unique distances
        unique_dists = sorted(list(set(dists)))
        
        def is_bipartite(threshold):
            # Build graph where edges exist if distance < threshold
            adj = collections.defaultdict(list)
            for i in range(n):
                x1, y1 = points[i]
                for j in range(i + 1, n):
                    x2, y2 = points[j]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    if d < threshold:
                        adj[i].append(j)
                        adj[j].append(i)
            
            # Standard bipartite check using BFS/DFS coloring
            color = {}
            for i in range(n):
                if i not in color:
                    color[i] = 0
                    queue = collections.deque([i])
                    while queue:
                        u = queue.popleft()
                        for v in adj[u]:
                            if v not in color:
                                color[v] = 1 - color[u]
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False
            return True

        # Binary search for the maximum distance threshold
        low = 0
        high = len(unique_dists) - 1
        ans = unique_dists[0]
        
        while low <= high:
            mid = (low + high) // 2
            if is_bipartite(unique_dists[mid]):
                ans = unique_dists[mid]
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
# @lc code=end