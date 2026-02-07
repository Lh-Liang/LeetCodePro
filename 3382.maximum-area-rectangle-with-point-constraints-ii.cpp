#
# @lc app=leetcode id=3382 lang=cpp
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        unordered_map<int, set<int>> coordMap;
        for (int i = 0; i < xCoord.size(); ++i) {
            coordMap[xCoord[i]].insert(yCoord[i]);
        }
        long long maxArea = -1;
        for (auto it1 = coordMap.begin(); it1 != coordMap.end(); ++it1) {
            auto x1 = it1->first;
            auto& ySet1 = it1->second;
            for (auto it2 = next(it1); it2 != coordMap.end(); ++it2) {
                auto x2 = it2->first;
                auto& ySet2 = it2->second;
                vector<int> commonYs;
                set_intersection(ySet1.begin(), ySet1.end(), ySet2.begin(), ySet2.end(), back_inserter(commonYs));
                if (commonYs.size() < 2) continue;
                for (int j = 0; j < commonYs.size(); ++j) {
                    for (int k = j + 1; k < commonYs.size(); ++k) {
                        int y1 = commonYs[j], y2 = commonYs[k];
                        long long area = abs(x2 - x1) * abs(y2 - y1);
                        bool validRectangle = true;
                        // Verify no other points are inside or on the borders
                        for (int l = 0; l < xCoord.size(); ++l) {
                            if ((xCoord[l] == x1 || xCoord[l] == x2) &&
                                (yCoord[l] == y1 || yCoord[l] == y2)) continue;
                            if (xCoord[l] > min(x1, x2) && xCoord[l] < max(x1, x2) &&
                                yCoord[l] > min(y1, y2) && yCoord[l] < max(y1, y2)) {
                                validRectangle = false;
                                break;
                            }
                        }
                        if (validRectangle && area > maxArea) maxArea = area;
                    }
                }
            }
        }
        return maxArea != -1 ? maxArea : -1;     } }; // @lc code=end