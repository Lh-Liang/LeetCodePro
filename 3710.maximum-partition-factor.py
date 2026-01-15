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
        
        # Compute all pairwise distances
        dists = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dists.append((d, i, j))
        
        dists.sort()
        unique_dists = sorted(set(d for d, i, j in dists))
        
        def is_bipartite(threshold):
            # Build graph with edges for dist < threshold
            adj = [[] for _ in range(n)]
            for d, i, j in dists:
                if d < threshold:
                    adj[i].append(j)
                    adj[j].append(i)
                else:
                    break  # Since dists is sorted
            
            color = [-1] * n
            for start in range(n):
                if color[start] == -1:
                    stack = [start]
                    color[start] = 0
                    while stack:
                        u = stack.pop()
                        for v in adj[u]:
                            if color[v] == -1:
                                color[v] = 1 - color[u]
                                stack.append(v)
                            elif color[v] == color[u]:
                                return False
            return True
        
        # Binary search to find the largest d such that is_bipartite(d) is True
        lo, hi = 0, len(unique_dists) - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            d = unique_dists[mid]
            if is_bipartite(d):
                ans = d
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
# @lc code=end