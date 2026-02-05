/*
 * @lc app=leetcode id=3382 lang=java
 *
 * [3382] Maximum Area Rectangle With Point Constraints II
 */

// @lc code=start
import java.util.*;
class Solution {
    public long maxRectangleArea(int[] xCoord, int[] yCoord) {
        int n = xCoord.length;
        Set<Long> pointSet = new HashSet<>();
        for (int i = 0; i < n; ++i) {
            pointSet.add(((long)xCoord[i] << 32) | (yCoord[i] & 0xffffffffL));
        }
        long maxArea = -1;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int x1 = xCoord[i], y1 = yCoord[i];
                int x2 = xCoord[j], y2 = yCoord[j];
                // Enforce canonical order to avoid duplicates: x1 < x2 and y1 < y2
                if (x1 >= x2 || y1 >= y2) continue;
                // Check if other two corners exist
                long p3 = (((long)x1) << 32) | (y2 & 0xffffffffL);
                long p4 = (((long)x2) << 32) | (y1 & 0xffffffffL);
                if (!pointSet.contains(p3) || !pointSet.contains(p4)) continue;
                boolean valid = true;
                for (int k = 0; k < n; ++k) {
                    // Skip the four corners
                    if ((xCoord[k] == x1 && yCoord[k] == y1) || (xCoord[k] == x2 && yCoord[k] == y2)
                        || (xCoord[k] == x1 && yCoord[k] == y2) || (xCoord[k] == x2 && yCoord[k] == y1)) continue;
                    int x = xCoord[k], y = yCoord[k];
                    // Check if point is inside or on the border
                    if (x >= x1 && x <= x2 && y >= y1 && y <= y2) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    long area = (long)(x2 - x1) * (y2 - y1);
                    maxArea = Math.max(maxArea, area);
                }
            }
        }
        return maxArea;
    }
}
// @lc code=end