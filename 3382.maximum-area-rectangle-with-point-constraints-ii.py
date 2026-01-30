#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = set(zip(xCoord, yCoord))
        n = len(xCoord)
        max_area = -1
        # For fast lookup, group coordinates by x and by y
        x_dict = {}
        y_dict = {}
        for x, y in points:
            x_dict.setdefault(x, set()).add(y)
            y_dict.setdefault(y, set()).add(x)
        # Only consider pairs of points from input data
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = xCoord[i], yCoord[i]
                x2, y2 = xCoord[j], yCoord[j]
                if x1 == x2 or y1 == y2:
                    continue
                # Consistent ordering to avoid duplicates
                x_low, x_high = sorted([x1, x2])
                y_low, y_high = sorted([y1, y2])
                # Check if rectangle corners exist
                if (x_low, y_high) not in points or (x_high, y_low) not in points:
                    continue
                # Check for other points strictly inside or on the border (excluding the four corners)
                has_inner = False
                # Only check actual points in dataset, not all in range
                for x, y in points:
                    if (x_low < x < x_high) and (y_low < y < y_high):
                        has_inner = True
                        break
                    # Border check (excluding corners)
                    if ((x == x_low or x == x_high) and (y_low < y < y_high)) or ((y == y_low or y == y_high) and (x_low < x < x_high)):
                        if (x, y) not in [(x_low, y_low), (x_low, y_high), (x_high, y_low), (x_high, y_high)]:
                            has_inner = True
                            break
                if not has_inner:
                    area = (x_high - x_low) * (y_high - y_low)
                    if area > max_area:
                        max_area = area
        return max_area
# @lc code=end