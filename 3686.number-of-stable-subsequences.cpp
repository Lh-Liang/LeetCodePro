#
# @lc app=leetcode id=3686 lang=cpp
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution {
public:
    int countStableSubsequences(vector<int>& nums) {
        long long dp[2][3] = {0}; // dp[parity][streak_length]
        // dp[0][1]: ends with Even, streak 1
        // dp[0][2]: ends with Even, streak 2
        // dp[1][1]: ends with Odd, streak 1
        // dp[1][2]: ends with Odd, streak 2
        
        const int MOD = 1e9 + 7;
        
        for (int x : nums) {
            int p = (x % 2 + 2) % 2; // Handle potential negative numbers if any, though constraints say >= 1
            
            if (p == 0) {
                // Current number is Even
                // 1. Form streak 1: Append to any Odd-ending subsequence or start new
                long long added_streak_1 = (dp[1][1] + dp[1][2] + 1) % MOD;
                
                // 2. Form streak 2: Append to any Even-ending subsequence with streak 1
                long long added_streak_2 = dp[0][1];
                
                // Update DP table
                dp[0][1] = (dp[0][1] + added_streak_1) % MOD;
                dp[0][2] = (dp[0][2] + added_streak_2) % MOD;
            } else {
                // Current number is Odd
                // 1. Form streak 1: Append to any Even-ending subsequence or start new
                long long added_streak_1 = (dp[0][1] + dp[0][2] + 1) % MOD;
                
                // 2. Form streak 2: Append to any Odd-ending subsequence with streak 1
                long long added_streak_2 = dp[1][1];
                
                // Update DP table
                dp[1][1] = (dp[1][1] + added_streak_1) % MOD;
                dp[1][2] = (dp[1][2] + added_streak_2) % MOD;
            }
        }
        
        long long total = (dp[0][1] + dp[0][2] + dp[1][1] + dp[1][2]) % MOD;
        return (int)total;
    }
};
# @lc code=end