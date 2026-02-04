#
# @lc app=leetcode id=3382 lang=cpp
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        unordered_map<int, unordered_set<int>> points;
        // Store all points in a map by their x-coordinate
        for (int i = 0; i < xCoord.size(); ++i) {
            points[xCoord[i]].insert(yCoord[i]);
        }
        long long maxArea = -1;
        // Iterate over pairs of different x-coordinates
        for (auto it1 = points.begin(); it1 != points.end(); ++it1) {
            for (auto it2 = std::next(it1); it2 != points.end(); ++it2) {
                int x1 = it1->first, x2 = it2->first;
                vector<int> commonYs;
                // Find common y-coordinates for these x-pairs
                for (int y : it1->second) {
                    if (it2->second.count(y)) {
                        commonYs.push_back(y);
                    }
                }
                // Need at least two common y-values to form a rectangle
                if (commonYs.size() < 2) continue;
                sort(commonYs.begin(), commonYs.end());
                // Check all pairs of y-values to form potential rectangles
                for (int j = 1; j < commonYs.size(); ++j) {
                    int y1 = commonYs[j-1], y2 = commonYs[j];
                    bool validRectangle = true;
                    // Ensure no other points within the potential rectangle's bounds
                    for (int k = min(x1,x2)+1; k < max(x1,x2); ++k) {
                        if ((points[k].count(y1)) || (points[k].count(y2))) { \\ Points on rectangle edges
                            validRectangle = false; \\ Invalidate rectangle if any point lies on border or inside
                            break;
                        }
                    }
                    if (!validRectangle) continue;
                    long long area = static_cast<long long>(abs(x2 - x1)) * static_cast<long long>(abs(y2 - y1));
                    maxArea = max(maxArea, area);
                }
            }
        }
        return maxArea == -1 ? -1 : maxArea; // Return correct maxArea value if found
    }
};
# @lc code=end