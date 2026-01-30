#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        from collections import defaultdict
        import heapq
        
        # Create adjacency list representation of the tree
        adj_list = defaultdict(list)
        total_weight = 0
        
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
            total_weight += w
        
        # Maximize sum by removing smallest weight edges if needed
        def reduce_connections(node):
            if len(adj_list[node]) <= k:
                return 0
            # Use a min-heap to remove smallest weights first
            excess_edges = len(adj_list[node]) - k
            min_heap = []
            for neighbor, weight in adj_list[node]:
                heapq.heappush(min_heap, (weight, neighbor))
                if len(min_heap) > excess_edges:
                    heapq.heappop(min_heap)  # Keep only excess_edges smallest elements in heap
            # Calculate reduction from these removed edges' weights
            reduction = sum(weight for weight, _ in min_heap)
            return reduction
        
        # Iterate over each node to reduce connections and calculate total reduction in weight. 
        total_reduction = 0
        for node in range(len(adj_list)):
            total_reduction += reduce_connections(node)
        
        # Return maximized sum of remaining weights after removal adjustments. 
n       return total_weight - total_reduction

# @lc code=end