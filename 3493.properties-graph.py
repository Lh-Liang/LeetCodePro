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

        # Pre-convert each property list to a set to count distinct integers efficiently
        property_sets = [set(p) for p in properties]
        
        # Compare all pairs to build the graph components
        for i in range(n):
            for j in range(i + 1, n):
                # Intersection of sets gives the distinct common integers
                if len(property_sets[i] & property_sets[j]) >= k:
                    union(i, j)
        
        # Count how many distinct roots exist in the DSU
        num_components = 0
        for i in range(n):
            if parent[i] == i:
                num_components += 1
                
        return num_components
# @lc code=end