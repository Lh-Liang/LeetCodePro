#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        from collections import defaultdict
        point_map = defaultdict(set)
        for x, y in zip(xCoord, yCoord):
            point_map[x].add(y)
        max_area = -1
        seen_pairs = {}
        for x in sorted(point_map):
            ys = sorted(point_map[x])
            for i in range(len(ys)):
                for j in range(i + 1, len(ys)):
                    y1, y2 = ys[i], ys[j]
                    if (y1, y2) in seen_pairs:
                        prev_x = seen_pairs[(y1, y2)]
                        area = (x - prev_x) * (y2 - y1)
                        # Perform additional checks here to ensure no point lies inside or on the border of this rectangle
                        if not any((prev_x < px < x or px == prev_x or px == x) and (y1 <= py <= y2) for px, py in zip(xCoord, yCoord)):
                            max_area = max(max_area, area)
                    seen_pairs[(y1, y2)] = x
        return max_area if max_area != -1 else -1
# @lc code=end