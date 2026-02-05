#
# @lc app=leetcode id=3743 lang=cpp
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution {
public:
    long long maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> arr(nums);
        arr.insert(arr.end(), nums.begin(), nums.end()); // duplicate for cyclic
        // Precompute range for all intervals of length up to n
        vector<vector<int>> maxv(2 * n, vector<int>(n + 1, INT_MIN));
        vector<vector<int>> minv(2 * n, vector<int>(n + 1, INT_MAX));
        for (int i = 0; i < 2 * n; ++i) {
            int mx = INT_MIN, mn = INT_MAX;
            for (int l = 1; l <= n && i + l - 1 < 2 * n; ++l) {
                mx = max(mx, arr[i + l - 1]);
                mn = min(mn, arr[i + l - 1]);
                maxv[i][l] = mx;
                minv[i][l] = mn;
            }
        }
        long long ans = 0;
        for (int st = 0; st < n; ++st) {
            vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, LLONG_MIN));
            dp[0][0] = 0;
            for (int i = 1; i <= n; ++i) {
                for (int p = 1; p <= k; ++p) {
                    for (int t = 1; t <= i; ++t) {
                        int l = i - t + 1;
                        long long range = maxv[st + l - 1][t] - minv[st + l - 1][t];
                        if (dp[i - t][p - 1] != LLONG_MIN)
                            dp[i][p] = max(dp[i][p], dp[i - t][p - 1] + range);
                    }
                }
            }
            for (int p = 1; p <= k; ++p)
                ans = max(ans, dp[n][p]);
        }
        return ans;
    }
};
# @lc code=end