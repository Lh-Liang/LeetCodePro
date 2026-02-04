# @lc app=leetcode id=3464 lang=cpp
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        auto check = [&](int d) -> bool {
            int count = 0;
            int n = points.size();
            // Sort points based on x and then y for consistent placement
            sort(points.begin(), points.end());
            vector<bool> used(n, false);
            for (int i = 0; i < n; ++i) {
                if (!used[i]) {
                    ++count;
                    used[i] = true;
                    // Mark all subsequent incompatible points within distance d
                    for (int j = i + 1; j < n; ++j) {
                        if (!used[j] && abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) < d) {
                            used[j] = true;
                        }
                    }
                }
                if (count >= k) return true;
            }
            return false;
        };
        
        int left = 0, right = side * 2 + 1; // Maximum possible Manhattan distance on square perimeter
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (check(mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
# @lc code=end