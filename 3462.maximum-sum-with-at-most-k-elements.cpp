#
# @lc app=leetcode id=3462 lang=cpp
#
# [3462] Maximum Sum With at Most K Elements
#
# @lc code=start
class Solution {
public:
    long long maxSum(vector<vector<int>>& grid, vector<int>& limits, int k) {
        int n = grid.size();
        vector<long long> dp(k + 1, 0);
        for (int i = 0; i < n; ++i) {
            vector<int> row = grid[i];
            sort(row.rbegin(), row.rend());
            vector<long long> prefix(1, 0);
            int lim = min((int)row.size(), limits[i]);
            for (int j = 0; j < lim; ++j) {
                prefix.push_back(prefix.back() + row[j]);
            }
            vector<long long> ndp = dp;
            for (int t = 1; t <= lim; ++t) {
                for (int x = k; x >= t; --x) {
                    ndp[x] = max(ndp[x], dp[x-t] + prefix[t]);
                }
            }
            dp = move(ndp);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
# @lc code=end