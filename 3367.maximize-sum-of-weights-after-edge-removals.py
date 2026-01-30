#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        import collections
        
        # Sort edges by weight descending
        edges.sort(key=lambda x: -x[2])
        
        total_weight = 0
        degree = collections.defaultdict(int)
        
        for u, v, w in edges:
            if degree[u] < k and degree[v] < k:
                # Add edge's weight to total if both nodes are under limit k
                total_weight += w
                degree[u] += 1
                degree[v] += 1
            # Skip any edge where adding it would violate the max connection rule for either node
            
        return total_weight 
# @lc code=end