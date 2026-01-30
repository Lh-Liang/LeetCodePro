#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#
from typing import List
from itertools import combinations

# @lc code=start
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        # Sort points by x-coordinate and y-coordinate separately,
        # this helps in considering extreme cases for partitions.
        x_sorted = sorted(points)
        y_sorted = sorted(points, key=lambda p: p[1])
        
        # Function to calculate manhattan distance
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        max_partition_factor = 0
        n = len(points)
        
        # Consider splits around different medians or quartiles potentially,
        # This is a place where specific geometric insights could help optimize.
        for i in range(1, n):
            # Split both sorted lists at different indices and calculate partition factors
            left_x = x_sorted[:i]
            right_x = x_sorted[i:]
            left_y = y_sorted[:i]
            right_y = y_sorted[i:]
            
            # Calculate minimal distances within each group for both splits,
            # select the best partition factor from different splits.
            def min_distance(group):
                if len(group) < 2:
                    return float('inf')
                return min(manhattan(p1, p2) for p1, p2 in combinations(group, 2))
            
            partition_factor_x = min(min_distance(left_x), min_distance(right_x))
            partition_factor_y = min(min_distance(left_y), min_distance(right_y))
            
            max_partition_factor = max(max_partition_factor, partition_factor_x, partition_factor_y)
        
        return max_partition_factor
# @lc code=end