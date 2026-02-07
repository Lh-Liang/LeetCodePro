#
# @lc app=leetcode id=3464 lang=cpp
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        // Helper function to check if we can select k points with at least minDist between any two
        auto canSelectKPoints = [&](int minDist) -> bool {
            // Check all combinations of selecting k points from given points array
            vector<int> selected;
            function<bool(int)> backtrack = [&](int start) {
                if (selected.size() == k) {
                    // Verify all pairs in selected meet or exceed minDist
                    for (int i = 0; i < selected.size(); ++i) {
                        for (int j = i + 1; j < selected.size(); ++j) {
                            int dist = abs(points[selected[i]][0] - points[selected[j]][0]) + abs(points[selected[i]][1] - points[selected[j]][1]);
                            if (dist < minDist) return false;
                        }
                    }
                    return true;
                }
                for (int i = start; i < points.size(); ++i) {
                    selected.push_back(i);
                    if (backtrack(i + 1)) return true;
                    selected.pop_back();
                }
                return false;
            };
            return backtrack(0);
        };
        
        int left = 0, right = side * 2; // Maximum possible Manhattan distance is twice the side length
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (canSelectKPoints(mid)) {
                left = mid; // If feasible, try for a larger minimum distance
            } else {
                right = mid - 1; // Otherwise, reduce search space
            }
        }
        return left;
    }
};
# @lc code=end