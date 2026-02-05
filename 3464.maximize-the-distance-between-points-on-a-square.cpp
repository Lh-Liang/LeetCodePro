#
# @lc app=leetcode id=3464 lang=cpp
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        // Precompute Manhattan distances between all pairs
        vector<vector<int>> dists(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dists[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
            }
        }
        // Helper to check if we can select k points with at least dist apart
        vector<int> chosen;
        function<bool(int, int)> dfs = [&](int idx, int cnt) {
            if (cnt == k) return true;
            if (n - idx < k - cnt) return false;
            for (int i = idx; i < n; ++i) {
                bool ok = true;
                for (int c : chosen) {
                    if (dists[c][i] < cur_d) { ok = false; break; }
                }
                if (ok) {
                    chosen.push_back(i);
                    if (dfs(i+1, cnt+1)) return true;
                    chosen.pop_back();
                }
            }
            return false;
        };
        int left = 0, right = 2*side, ans = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            int cur_d = mid;
            chosen.clear();
            // Capture cur_d in lambda
            bool possible = false;
            auto dfs2 = [&](auto&& self, int idx, int cnt) -> bool {
                if (cnt == k) return true;
                if (n - idx < k - cnt) return false;
                for (int i = idx; i < n; ++i) {
                    bool ok = true;
                    for (int c : chosen) {
                        if (dists[c][i] < cur_d) { ok = false; break; }
                    }
                    if (ok) {
                        chosen.push_back(i);
                        if (self(self, i+1, cnt+1)) return true;
                        chosen.pop_back();
                    }
                }
                return false;
            };
            if (dfs2(dfs2, 0, 0)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }
};
# @lc code=end