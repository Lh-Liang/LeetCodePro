#
# @lc app=leetcode id=3538 lang=cpp
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution {
public:
    int minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        // Initialize DP table where dp[i][j] is the min travel time using i merges up to j-th sign.
        vector<vector<int>> dp(k + 1, vector<int>(n, INT_MAX));
        
        // Calculate initial travel time without any merges.
        dp[0][0] = 0;
        for (int j = 1; j < n; ++j) {
            dp[0][j] = dp[0][j-1] + time[j-1] * (position[j] - position[j-1]);
        }
        
        // Fill DP table for each number of merges from 1 to k.
        for (int i = 1; i <= k; ++i) {
            for (int j = i+1; j < n; ++j) { // Ensure sufficient elements for merging
                for (int x = i; x < j; ++x) { // Consider merging segments ending at x and starting at x+1.
                    int merged_time = time[x - 1] + time[x];
                    int segment_length = position[j] - position[x]; // Corrected index access
                    dp[i][j] = min(dp[i][j], dp[i-1][x-1] + merged_time * segment_length);
                }
            }
        }
        
        return dp[k][n-1]; // Return min travel time with exactly k merges up to last sign.
    }
};
# @lc code=end