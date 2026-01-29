#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        # Convert to sets to ensure we count 'distinct integers common to both'
        sets = [set(p) for p in properties]
        
        # DSU implementation
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
        
        components = n
        # Check all pairs for edges
        for i in range(n):
            for j in range(i + 1, n):
                # Intersection of sets gives distinct common elements
                if len(sets[i] & sets[j]) >= k:
                    if union(i, j):
                        components -= 1
        
        return components
# @lc code=end