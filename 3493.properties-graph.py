#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
        for i in range(n):
            for j in range(i + 1, n):
                inter = len(set(properties[i]) & set(properties[j]))
                if inter >= k:
                    union(i, j)
        roots = set(find(i) for i in range(n))
        return len(roots)
# @lc code=end