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
        
        # Calculate all pairwise distances
        distances = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append((dist, i, j))
        
        distances.sort()
        unique_distances = sorted(set([d[0] for d in distances] + [0]))
        
        def can_partition(threshold):
            # Build adjacency list for graph where edges connect points with distance < threshold
            adj = [[] for _ in range(n)]
            for dist, i, j in distances:
                if dist < threshold:
                    adj[i].append(j)
                    adj[j].append(i)
                else:
                    break
            
            # Check if graph is bipartite using BFS
            color = [-1] * n
            
            for start in range(n):
                if color[start] != -1:
                    continue
                
                queue = [start]
                color[start] = 0
                
                while queue:
                    u = queue.pop(0)
                    for v in adj[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False
            
            return True
        
        # Binary search on the distance values
        left, right = 0, len(unique_distances) - 1
        result = 0
        
        while left <= right:
            mid_idx = (left + right) // 2
            threshold = unique_distances[mid_idx]
            if can_partition(threshold):
                result = threshold
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        
        return result
# @lc code=end