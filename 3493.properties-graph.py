#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        # Convert each property list into a set to handle distinct integers efficiently
        node_sets = [set(p) for p in properties]
        # Initialize Disjoint Set Union (DSU) parent pointers
        parent = list(range(n))
        
        def find(x):
            # Standard find with path compression
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        num_components = n
        # Iterate through all unique pairs of nodes
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the number of distinct common integers using set intersection
                if len(node_sets[i] & node_sets[j]) >= k:
                    root_i = find(i)
                    root_j = find(j)
                    # If nodes are in different components, merge them
                    if root_i != root_j:
                        parent[root_i] = root_j
                        num_components -= 1
                        
        return num_components
# @lc code=end