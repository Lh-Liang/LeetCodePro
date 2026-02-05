#
# @lc app=leetcode id=3686 lang=cpp
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution {
public:
    int countStableSubsequences(vector<int>& nums) {
        static const int MOD = 1e9 + 7;
        // dp[last_parity][run] = number of ways
        // run = 0 (no element), 1 (one in a row), 2 (two in a row)
        vector<vector<int>> dp(2, vector<int>(3, 0));
        dp[0][0] = dp[1][0] = 1; // empty subsequence (for transition)
        for (int x : nums) {
            int p = x % 2;
            vector<vector<int>> ndp(2, vector<int>(3, 0));
            // For every possible previous state
            for (int last_p = 0; last_p <= 1; ++last_p) {
                for (int run = 0; run <= 2; ++run) {
                    int val = dp[last_p][run];
                    if (!val) continue;
                    // Option 1: skip (carry over)
                    ndp[last_p][run] = (ndp[last_p][run] + val) % MOD;
                    // Option 2: take
                    if (run < 2 && last_p == p) {
                        ndp[p][run+1] = (ndp[p][run+1] + val) % MOD;
                    }
                    if (last_p != p) {
                        ndp[p][1] = (ndp[p][1] + val) % MOD;
                    }
                }
            }
            dp = ndp;
        }
        // Remove empty subsequence
        int ans = 0;
        for (int p = 0; p <= 1; ++p)
            for (int run = 1; run <= 2; ++run)
                ans = (ans + dp[p][run]) % MOD;
        return ans;
    }
};
# @lc code=end