#
# @lc app=leetcode id=3382 lang=cpp
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        unordered_set<long long> pointSet;
        int n = xCoord.size();
        // Combine x and y into a single hashable integer (offset multiplier > max y)
        const long long OFFSET = 80000010LL;
        for (int i = 0; i < n; ++i) {
            pointSet.insert(xCoord[i] * OFFSET + yCoord[i]);
        }
        long long maxArea = -1;
        // Use a map to group all y's for each x, and x's for each y (optional, can help for optimization)
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int x1 = xCoord[i], y1 = yCoord[i];
                int x2 = xCoord[j], y2 = yCoord[j];
                if (x1 == x2 || y1 == y2) continue; // must be diagonal
                // get other two corners
                if (!pointSet.count(x1 * OFFSET + y2) || !pointSet.count(x2 * OFFSET + y1)) continue;
                // Check if any other point is inside or on border (besides the corners)
                int minX = min(x1, x2), maxX = max(x1, x2);
                int minY = min(y1, y2), maxY = max(y1, y2);
                bool valid = true;
                // Only need to check if any point other than the four corners lies inside/on the border
                for (int k = 0; k < n; ++k) {
                    int px = xCoord[k], py = yCoord[k];
                    // skip rectangle corners
                    if ((px == x1 && py == y1) || (px == x2 && py == y2) || (px == x1 && py == y2) || (px == x2 && py == y1)) continue;
                    if (px >= minX && px <= maxX && py >= minY && py <= maxY) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    long long area = (long long)(maxX - minX) * (maxY - minY);
                    if (area > maxArea) maxArea = area;
                }
            }
        }
        return maxArea;
    }
};
# @lc code=end