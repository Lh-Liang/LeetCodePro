#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        # Pre-convert each row to a set to handle distinct integers and speed up intersections
        sets = [set(p) for p in properties]
        
        # Union-Find data structure initialization
        parent = list(range(n))
        components = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            nonlocal components
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                components -= 1
                return True
            return False
        
        # Iterate through all unique pairs of nodes
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate distinct integers common to both arrays
                common_count = len(sets[i] & sets[j])
                
                # If condition met, add an edge (union the components)
                if common_count >= k:
                    union(i, j)
                    
        return components
# @lc code=end