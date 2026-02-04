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
        // dp[i][last_parity][consecutive]:
        // Number of ways up to i, last selected element has parity last_parity, consecutive same parity elements
        vector<vector<vector<int>>> dp(n+1, vector<vector<int>>(2, vector<int>(3, 0)));
        // Base case: no elements selected yet
        dp[0][0][0] = dp[0][1][0] = 1; // 1 way: empty subsequence
        for (int i = 0; i < n; ++i) {
            int p = nums[i] % 2;
            for (int last=0; last<2; ++last) {
                for (int c=0; c<3; ++c) {
                    int ways = dp[i][last][c];
                    if (!ways) continue;
                    // Skip nums[i]
                    dp[i+1][last][c] = (dp[i+1][last][c] + ways) % MOD;
                    // Pick nums[i]
                    if (c < 2 && last == p) {
                        dp[i+1][p][c+1] = (dp[i+1][p][c+1] + ways) % MOD;
                    } else if (last != p) {
                        dp[i+1][p][1] = (dp[i+1][p][1] + ways) % MOD;
                    }
                }
            }
        }
        int ans = 0;
        // Sum all non-empty subsequences
        for (int last=0; last<2; ++last) {
            for (int c=1; c<3; ++c) {
                ans = (ans + dp[n][last][c]) % MOD;
            }
        }
        return ans;
    }
};
# @lc code=end