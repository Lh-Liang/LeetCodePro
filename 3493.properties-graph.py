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
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        # Convert each property list to a set to handle 'distinct' elements and speed up intersection
        sets = [set(p) for p in properties]
        components = n
        
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate number of distinct integers common to both using set intersection
                if len(sets[i].intersection(sets[j])) >= k:
                    if union(i, j):
                        components -= 1
                        
        return components
# @lc code=end