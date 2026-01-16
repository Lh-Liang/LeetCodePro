#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        # Combine coordinates into a set for O(1) lookup
        points = set(zip(xCoord, yCoord))
        n = len(xCoord)
        max_area = -1
        
        # Try all pairs of points as potential diagonals
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = xCoord[i], yCoord[i]
                x2, y2 = xCoord[j], yCoord[j]
                
                # Skip if points are on same horizontal or vertical line
                # (they can't form a diagonal of a rectangle)
                if x1 == x2 or y1 == y2:
                    continue
                
                # Check if the other two corners exist to form a rectangle
                if (x1, y2) in points and (x2, y1) in points:
                    # We have a valid rectangle with corners at:
                    # (x1,y1), (x1,y2), (x2,y1), (x2,y2)
                    
                    # Check if any other point lies inside or on the border
                    valid = True
                    
                    # Determine the boundaries of the rectangle
                    min_x, max_x = min(x1, x2), max(x1, x2)
                    min_y, max_y = min(y1, y2), max(y1, y2)
                    
                    # Check all points to see if any lie inside/on the rectangle
                    for k in range(n):
                        x, y = xCoord[k], yCoord[k]
                        # Skip the four corners of our rectangle
                        if (x == x1 and y == y1) or (x == x1 and y == y2) or \
                           (x == x2 and y == y1) or (x == x2 and y == y2):
                            continue
                        
                        # Check if point is inside or on the border
                        if min_x <= x <= max_x and min_y <= y <= max_y:
                            valid = False
                            break
                    
                    if valid:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        max_area = max(max_area, area)
        
        return max_area
# @lc code=end