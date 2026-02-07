#
# @lc app=leetcode id=3686 lang=cpp
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution {
public:
    int countStableSubsequences(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int n = nums.size();
        vector<vector<int>> dp(n+1, vector<int>(2, 0)); // dp[i][0] = count ending in even, dp[i][1] = count ending in odd
        dp[0][0] = dp[0][1] = 1; // empty sequence counts as 1 valid subsequence
        
        for (int i = 1; i <= n; ++i) {
            int parity = nums[i-1] % 2; // current number's parity
            if (parity == 0) { // even number
                dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD; // can continue any sequence or start new with even end
                dp[i][1] = dp[i-1][1]; // odd-ending sequences remain same as they can't end with current even number without breaking rules
            } else { // odd number
                dp[i][0] = dp[i-1][0]; // even-ending sequences remain same as they can't end with current odd number without breaking rules
                dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD; // can continue any sequence or start new with odd end
            }
        }
        
        return (dp[n][0] + dp[n][1] - 1) % MOD; // subtract one to exclude the empty subsequence counted initially.
    }
};
# @lc code=end