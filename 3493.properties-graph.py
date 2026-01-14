#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        
        # Convert each property to a set of distinct elements
        property_sets = [set(prop) for prop in properties]
        
        # Union-Find
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate intersection size
                common = len(property_sets[i] & property_sets[j])
                if common >= k:
                    union(i, j)
        
        # Count unique components
        return len(set(find(i) for i in range(n)))
# @lc code=end