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
        vector<vector<long long>> dp(n, vector<long long>(k + 1, LLONG_MIN));
        
        // Initialize base case for one partition (full range)
        for (int start = 0; start < n; ++start) {
            int minVal = INT_MAX, maxVal = INT_MIN;
            for (int end = start; end < start + n; ++end) {
                minVal = min(minVal, nums[end % n]);
                maxVal = max(maxVal, nums[end % n]);
                if (end - start + 1 <= n) { // Ensure not exceeding cyclic wrap
                    dp[end % n][1] = max(dp[end % n][1], (long long)(maxVal - minVal));
                }
            }
        }

        // Fill DP table considering cyclic nature efficiently using modulo
        for (int j = 2; j <= k; ++j) {
            for (int end = 0; end < n; ++end) {
                int minVal = INT_MAX, maxVal = INT_MIN;
                for (int split = end + n - 1; split >= end; --split) {
                    minVal = min(minVal, nums[split % n]);
                    maxVal = max(maxVal, nums[split % n]);
                    if ((split + n - end) % n > 0 && dp[(split-1+n)%n][j-1] != LLONG_MIN) { // Ensure valid split point and previous state exists
                        dp[end][j] = max(dp[end][j], dp[(split-1+n)%n][j-1] + (maxVal - minVal));
                    }
                }
            }
        }

        // Find maximum possible score with up to k partitions
        long long result = LLONG_MIN;
        for(int i = 0; i < n; ++i) {
            result = max(result, dp[i][k]);
        }
        return result;
    }
};
# @lc code=end