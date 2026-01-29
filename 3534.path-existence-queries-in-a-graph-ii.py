#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        # Sort nodes based on their nums values
        sorted_nodes = sorted(range(n), key=lambda x: nums[x])
        
        # Initialize union-find structure
        parent = list(range(n))
        rank = [0] * n
        
        # Create edges in sorted order to ensure efficiency
        for i in range(n):
            for j in range(i + 1, n):
                if nums[sorted_nodes[j]] - nums[sorted_nodes[i]] > maxDiff:
                    break  # No need to check further due to sorting
                union(sorted_nodes[i], sorted_nodes[j])
        
        # Answer each query using the union-find structure
        answer = []
        for u, v in queries:
            if find(u) == find(v):
                answer.append(1)  # Nodes are connected within maxDiff constraint
            else:
                answer.append(-1)  # Nodes are not connected
            
        return answer
# @lc code=end