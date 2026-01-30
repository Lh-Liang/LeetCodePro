#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Union-Find (Disjoint Set Union) implementation
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
        
        # Sort nodes by their nums value for efficient edge creation
        sorted_nodes = sorted(range(n), key=lambda x: nums[x])
        
        # Create edges using two-pointer technique on sorted nodes
        j = 0
        for i in range(n):
            while j < n and nums[sorted_nodes[j]] - nums[sorted_nodes[i]] <= maxDiff:
                union(sorted_nodes[i], sorted_nodes[j])
                j += 1
        
        # Answer queries using union-find results
        answer = []
        for ui, vi in queries:
            if find(ui) == find(vi):
                answer.append(1)
            else:
                answer.append(-1)
        return answer
# @lc code=end