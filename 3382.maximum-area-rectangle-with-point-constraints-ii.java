# @lc app=leetcode id=3382 lang=java
#
# [3382] Maximum Area Rectangle With Point Constraints II
#
# @lc code=start
class Solution {
    public long maxRectangleArea(int[] xCoord, int[] yCoord) {
        Set<String> pointSet = new HashSet<>();
        for (int i = 0; i < xCoord.length; i++) {
            pointSet.add(xCoord[i] + "_" + yCoord[i]);
        }
        long maxArea = -1;
        for (int i = 0; i < xCoord.length; i++) {
            for (int j = i + 1; j < xCoord.length; j++) {
                int x1 = xCoord[i], y1 = yCoord[i];
                int x2 = xCoord[j], y2 = yCoord[j];
                if (x1 != x2 && y1 != y2) {  // Check for diagonal corners
                    if (pointSet.contains(x1 + "_" + y2) && pointSet.contains(x2 + "_" + y1)) {
                        long area = Math.abs((long)(x2 - x1) * (y2 - y1));
                        if (area > maxArea) {
                            maxArea = area;
                        }
                    }
                }
            }
        }
        return maxArea;
    }
}
# @lc code=end