#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
from typing import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Initialize Union-Find structure
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
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
        
        # Step 2 and 3: Sort and construct edges using sliding window technique
        indexed_nums = sorted((num, index) for index, num in enumerate(nums))
        i = 0
        for j in range(n):
            while indexed_nums[j][0] - indexed_nums[i][0] > maxDiff:
                i += 1
            # Union all nodes within current window satisfying condition
            for k in range(i, j):
                union(indexed_nums[k][1], indexed_nums[j][1])
        
        # Step 5: Process each query using Union-Find results
        result = []
        for ui, vi in queries:
            if find(ui) == find(vi):
                result.append(1)
            else:
                result.append(-1)
        return result
# @lc code=end