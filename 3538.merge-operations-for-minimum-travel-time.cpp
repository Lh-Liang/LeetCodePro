#
# @lc app=leetcode id=3538 lang=cpp
#
# [3538] Merge Operations for Minimum Travel Time
#
# @lc code=start
class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        vector<vector<int>> dp(n, vector<int>(k + 1, INT_MAX));
        // Calculate initial travel times with no merges
        for (int i = 0; i < n - 1; ++i) {
            dp[i + 1][0] = (position[i + 1] - position[i]) * time[i];
            if (i > 0) {
                dp[i + 1][0] += dp[i][0];
            }
        }
        // Fill DP table for each merge count from 1 to k
        for (int m = 1; m <= k; ++m) {
            for (int i = m + 1; i < n; ++i) {
                // Consider merging segments at current end position i
                for (int j = m; j < i; ++j) {
                    int mergedTime = (position[i] - position[j]) * (time[j - 1] + time[j]);
                    dp[i][m] = min(dp[i][m], dp[j - 1][m - 1] + mergedTime);
                }
            }
        }
        return dp[n-1][k];
    }
};
# @lc code=end