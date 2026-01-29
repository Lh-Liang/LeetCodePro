#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        import itertools
        # Function to calculate Manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Initialize max partition factor to zero
        max_partition_factor = 0
        n = len(points)
        
        # Iterate over all possible ways to split points into two groups
        for i in range(1, (1 << n) // 2):
            group1 = [points[j] for j in range(n) if (i & (1 << j))]
            group2 = [points[j] for j in range(n) if not (i & (1 << j))]
            
            # Compute minimum intra-group distance for each group
            min_dist_group1 = float('inf') if len(group1) > 1 else 0
            min_dist_group2 = float('inf') if len(group2) > 1 else 0
            
            for p1, p2 in itertools.combinations(group1, 2):
                min_dist_group1 = min(min_dist_group1, manhattan_distance(p1, p2))
            for p1, p2 in itertools.combinations(group2, 2):
                min_dist_group2 = min(min_dist_group2, manhattan_distance(p1, p2))
            
            # Calculate partition factor for this split and update maximum found so far
            current_partition_factor = min(min_dist_group1, min_dist_group2)
            max_partition_factor = max(max_partition_factor, current_partition_factor)
        
        return max_partition_factor
# @lc code=end