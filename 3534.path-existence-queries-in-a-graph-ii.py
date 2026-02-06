#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Initialize Union-Find structure
        parent = list(range(n))
        rank = [0] * n
        
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
        
        # Connect nodes within maxDiff constraint
        sorted_nodes = sorted(range(n), key=lambda i: nums[i])
        for i in range(n):
            for j in range(i + 1, n):
                if nums[sorted_nodes[j]] - nums[sorted_nodes[i]] <= maxDiff:
                    union(sorted_nodes[i], sorted_nodes[j])
                else:
                    break  # No need to check further as list is sorted by value difference exceeds maxDiff.
        
        answer = []
        for u, v in queries:
            if find(u) == find(v):
                answer.append(1)  # Path exists between u and v. (connected)
            else:
                answer.append(-1)  # No path exists between u and v. (disconnected) "return answer\\# @lc code=end