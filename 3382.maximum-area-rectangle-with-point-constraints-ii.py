#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = set(zip(xCoord, yCoord))
        
        # Group points by x-coordinate
        by_x = defaultdict(set)
        for x, y in points:
            by_x[x].add(y)
        
        xs = sorted(by_x.keys())
        max_area = -1
        
        # Try all pairs of x-coordinates
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                x1, x2 = xs[i], xs[j]
                
                # Find common y-coordinates (potential rectangle corners)
                common_ys = sorted(by_x[x1] & by_x[x2])
                
                # Try all pairs of common y-coordinates
                for k in range(len(common_ys)):
                    for l in range(k + 1, len(common_ys)):
                        y1, y2 = common_ys[k], common_ys[l]
                        
                        # Check if any other point is inside or on the border
                        valid = True
                        for x in xs:
                            if x < x1 or x > x2:
                                continue
                            for y in by_x[x]:
                                if y < y1 or y > y2:
                                    continue
                                # This point is inside or on border
                                if (x, y) not in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                                    valid = False
                                    break
                            if not valid:
                                break
                        
                        if valid:
                            area = (x2 - x1) * (y2 - y1)
                            max_area = max(max_area, area)
        
        return max_area
# @lc code=end