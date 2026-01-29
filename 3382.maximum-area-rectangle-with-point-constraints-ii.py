# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        from collections import defaultdict
        
        # Store each point in a set for quick lookup
        points = set(zip(xCoord, yCoord))
        n = len(xCoord)
        max_area = -1  # Initialize max_area as -1
        
        # Iterate over all pairs of points (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                # Ensure they form diagonal corners (x-coordinates and y-coordinates must differ)
                if xCoord[i] != xCoord[j] and yCoord[i] != yCoord[j]:
                    # Check both opposite diagonal corners exist in set
                    p1 = (xCoord[i], yCoord[j])
                    p2 = (xCoord[j], yCoord[i])
                    if p1 in points and p2 in points:
                        # Calculate area of this potential rectangle
                        area = abs(xCoord[i] - xCoord[j]) * abs(yCoord[i] - yCoord[j])
                        
                        # Check for no internal points by iterating through all other points
                        has_internal_points = False
                        for k in range(n):
                            # Skip corner checks already verified above
                            if k == i or k == j or (xCoord[k], yCoord[k]) == p1 or (xCoord[k], yCoord[k]) == p2:
                                continue
                            # Check if point k is inside the rectangle bounds (exclusive)
                            if (min(xCoord[i], xCoord[j]) < xCoord[k] < max(xCoord[i], xCoord[j])) and \
                               (min(yCoord[i], yCoord[j]) < yCoord[k] < max(yCoord[i], yCoord[j])):
                                has_internal_points = True
                                break
                        
                        if not has_internal_points:
                            max_area = max(max_area, area)  # Update max_area if larger found
        return max_area  # Return the maximum found or -1 if no valid rectangle found
# @lc code=end