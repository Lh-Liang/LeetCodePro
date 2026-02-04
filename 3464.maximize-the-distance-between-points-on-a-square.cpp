#
# @lc app=leetcode id=3464 lang=cpp
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        // Binary search template for answer
        int n = points.size();
        // Precompute all pairwise Manhattan distances
        vector<vector<int>> dist(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dist[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
            }
        }
        // Helper: can we select k points with at least 'd' min distance?
        function<bool(int)> can = [&](int d) {
            vector<int> idxs;
            function<bool(int, int)> dfs = [&](int pos, int chosen) {
                if (chosen == k) return true;
                if (n - pos < k - chosen) return false;
                for (int i = pos; i < n; ++i) {
                    bool ok = true;
                    for (int idx : idxs) {
                        if (dist[i][idx] < d) { ok = false; break; }
                    }
                    if (ok) {
                        idxs.push_back(i);
                        if (dfs(i+1, chosen+1)) return true;
                        idxs.pop_back();
                    }
                }
                return false;
            };
            idxs.clear();
            return dfs(0,0);
        };
        int lo = 0, hi = 2*side+1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (can(mid)) lo = mid+1;
            else hi = mid;
        }
        return lo-1;
    }
};
# @lc code=end