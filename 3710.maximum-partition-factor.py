#
# @lc app=leetcode id=3710 lang=python3
#
# [3710] Maximum Partition Factor
#

from typing import List

# @lc code=start
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        if n == 2:
            return manhattan(points[0], points[1])
        
        # Considering properties of Manhattan distance in sorted arrays
        # Sort by x+y and x-y coordinates respectively
        transformed_1 = sorted(points, key=lambda p: p[0] + p[1])
        transformed_2 = sorted(points, key=lambda p: p[0] - p[1])
        
        max_factor = 0
        # Check both transformations for potential optimal splits
        for transformed in [transformed_1, transformed_2]:
            # Check splitting at each point in the sorted order except the last one
            for i in range(1, n):
                group_1 = transformed[:i]
                group_2 = transformed[i:]
                # Calculate minimum intra-group Manhattan distances for both groups
                min_distance_1 = float('inf') if len(group_1) > 1 else 0
                min_distance_2 = float('inf') if len(group_2) > 1 else 0
                
                for j in range(len(group_1)):
                    for k in range(j + 1, len(group_1)):
                        min_distance_1 = min(min_distance_1, manhattan(group_1[j], group_1[k]))
                for j in range(len(group_2)):
                    for k in range(j + 1, len(group_2)):
                        min_distance_2 = min(min_distance_2, manhattan(group_2[j], group_2[k]))
                
                # Maximize partition factor which is the minimum of these two distances
                max_factor = max(max_factor, min(min_distance_1, min_distance_2))

        return max_factor
# @lc code=end