#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        # Step 1: Store all points in a set for O(1) lookups
        points = set(zip(xCoord, yCoord))
        n = len(xCoord)
        max_area = -1
        # Step 2: Iterate over all pairs of points as possible diagonal corners
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = xCoord[i], yCoord[i]
                x2, y2 = xCoord[j], yCoord[j]
                # Only consider rectangles, not lines
                if x1 == x2 or y1 == y2:
                    continue
                # Ensure the other two corners exist
                if (x1, y2) in points and (x2, y1) in points:
                    # Step 3: Check for any point strictly inside or on the border except corners
                    inside = False
                    min_x, max_x = min(x1, x2), max(x1, x2)
                    min_y, max_y = min(y1, y2), max(y1, y2)
                    # For efficiency, skip corners
                    for k in range(n):
                        px, py = xCoord[k], yCoord[k]
                        if (px, py) in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                            continue
                        if min_x <= px <= max_x and min_y <= py <= max_y:
                            inside = True
                            break
                    if not inside:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        max_area = max(max_area, area)
        return max_area
# @lc code=end