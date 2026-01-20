#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
from typing import List


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        props = [set(p) for p in properties]
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True
        
        components = n
        for i in range(n):
            for j in range(i + 1, n):
                if len(props[i] & props[j]) >= k:
                    if union(i, j):
                        components -= 1
        
        return components

# @lc code=end
