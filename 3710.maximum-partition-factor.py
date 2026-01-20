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
        
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        edges.sort(key=lambda x: x[0])
        
        parent = list(range(n))
        # diff[i] stores the color difference between node i and parent[i]
        # 0 means same color, 1 means different color
        diff = [0] * n
        
        def find(i):
            if parent[i] != i:
                root, root_diff = find(parent[i])
                parent[i] = root
                diff[i] = diff[i] ^ root_diff
            return parent[i], diff[i]
        
        for w, u, v in edges:
            root_u, d_u = find(u)
            root_v, d_v = find(v)
            
            if root_u != root_v:
                # Merge components
                # We want color[u] != color[v]
                # color[u] = color[root_u] ^ d_u
                # color[v] = color[root_v] ^ d_v
                # We want (color[root_u] ^ d_u) != (color[root_v] ^ d_v)
                # => color[root_u] ^ color[root_v] = d_u ^ d_v ^ 1
                # Let's attach root_u to root_v
                parent[root_u] = root_v
                diff[root_u] = d_u ^ d_v ^ 1
            else:
                # Same component
                # Check if valid
                if d_u == d_v:
                    # Same parity relative to root => same color => conflict
                    return w
                    
        return 0
# @lc code=end