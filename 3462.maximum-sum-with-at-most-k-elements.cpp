#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        if (k == 0) return 0LL;

        int n = (int)grid.size();
        long long totalCap = 0;
        for (int i = 0; i < n; i++) {
            totalCap += min(limits[i], (int)grid[i].size());
        }

        vector<int> cand;
        cand.reserve((size_t)totalCap);

        for (int i = 0; i < n; i++) {
            int m = (int)grid[i].size();
            int t = min(limits[i], m);
            if (t <= 0) continue;

            auto &row = grid[i];
            if (t == m) {
                cand.insert(cand.end(), row.begin(), row.end());
            } else {
                nth_element(row.begin(), row.begin() + t, row.end(), greater<int>());
                for (int j = 0; j < t; j++) cand.push_back(row[j]);
            }
        }

        if (cand.empty()) return 0LL;

        if (k >= (int)cand.size()) {
            long long ans = 0;
            for (int v : cand) ans += v;
            return ans;
        }

        nth_element(cand.begin(), cand.begin() + k, cand.end(), greater<int>());
        long long ans = 0;
        for (int i = 0; i < k; i++) ans += cand[i];
        return ans;
    }
};
# @lc code=end
