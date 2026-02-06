#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(a: List[int], b: List[int]) -> int:
            return len(set(a) & set(b))
        n = len(properties)
        uf = list(range(n))
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                uf[rootX] = rootY
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    union(i, j)
        return len(set(find(x) for x in range(n))) 
# @lc code=end