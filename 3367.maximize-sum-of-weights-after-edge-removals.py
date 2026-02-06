#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        from collections import defaultdict
        # Create graph with node connections count
        node_connections = defaultdict(int)
        # Sort edges by weights in descending order to maximize sum when added
        edges.sort(key=lambda x: x[2], reverse=True)
        # Initialize max sum of weights
        max_weight_sum = 0
        for u, v, w in edges:
            if node_connections[u] < k and node_connections[v] < k:
                # Add edge if both nodes have less than k connections
                max_weight_sum += w
                node_connections[u] += 1
                node_connections[v] += 1
        return max_weight_sum
# @lc code=end