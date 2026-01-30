#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = set(zip(xCoord, yCoord))
        max_area = -1
        n = len(xCoord)
        for i in range(n):
            for j in range(i + 1, n):
                if xCoord[i] != xCoord[j] and yCoord[i] != yCoord[j]:  # Ensure different x and y to form diagonal
                    if (xCoord[i], yCoord[j]) in points and (xCoord[j], yCoord[i]) in points:
                        area = abs(xCoord[i] - xCoord[j]) * abs(yCoord[i] - yCoord[j])
                        max_area = max(max_area, area)
        return max_area if max_area != -1 else -1
# @lc code=end