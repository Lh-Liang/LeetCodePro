#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        point_set = set(zip(xCoord, yCoord))
        max_area = -1
        for i in range(len(xCoord)):
            for j in range(i + 1, len(xCoord)):
                if xCoord[i] != xCoord[j] and yCoord[i] != yCoord[j]:
                    if ((xCoord[i], yCoord[j]) in point_set) and ((xCoord[j], yCoord[i]) in point_set):
                        area = abs(xCoord[i] - xCoord[j]) * abs(yCoord[i] - yCoord[j])
                        max_area = max(max_area, area)
        return max_area if max_area != -1 else -1
# @lc code=end