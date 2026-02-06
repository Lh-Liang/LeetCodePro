#
# @lc app=leetcode id=3382 lang=java
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
import java.util.*;
class Solution {
    public long maxRectangleArea(int[] xCoord, int[] yCoord) {
        int n = xCoord.length;
        Set<Long> points = new HashSet<>();
        // Encode point: (x, y) -> ((long)x << 32) | y
        for (int i = 0; i < n; ++i) {
            points.add(((long)xCoord[i] << 32) | (yCoord[i] & 0xffffffffL));
        }
        long maxArea = -1;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int x1 = xCoord[i], y1 = yCoord[i];
                int x2 = xCoord[j], y2 = yCoord[j];
                if (x1 == x2 || y1 == y2) continue; // must be diagonal
                // Compute the other two corners
                long p3 = ((long)x1 << 32) | (y2 & 0xffffffffL);
                long p4 = ((long)x2 << 32) | (y1 & 0xffffffffL);
                if (!points.contains(p3) || !points.contains(p4)) continue;
                // Now check if any other point lies inside or on the border
                int minX = Math.min(x1, x2), maxX = Math.max(x1, x2);
                int minY = Math.min(y1, y2), maxY = Math.max(y1, y2);
                boolean valid = true;
                for (int k = 0; k < n; ++k) {
                    int x = xCoord[k], y = yCoord[k];
                    if ((x == x1 && y == y1) || (x == x2 && y == y2) || (x == x1 && y == y2) || (x == x2 && y == y1)) continue;
                    if (x >= minX && x <= maxX && y >= minY && y <= maxY) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    long area = (long)(maxX - minX) * (maxY - minY);
                    if (area > maxArea) maxArea = area;
                }
            }
        }
        return maxArea;
    }
}
# @lc code=end