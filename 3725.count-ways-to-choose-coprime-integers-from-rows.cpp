#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        const int MOD = 1e9 + 7;
        int m = mat.size();
        vector<int> dp(151, 0); // dp[g] represents how many ways we can choose numbers with gcd g
        dp[1] = 1; // Initialize with gcd of 1 as valid starting point
        for (const auto &row : mat) {
            vector<int> new_dp(151, 0);
            for (int num : row) {
                for (int g = 1; g <= 150; ++g) {
                    int new_gcd = gcd(num, g);
                    new_dp[new_gcd] = (new_dp[new_gcd] + dp[g]) % MOD;
                }
            }
            dp = new_dp; // Update dp array for next row processing
        }
        return dp[1]; // Number of ways with GCD as 1 is the result needed.
    }
};
# @lc code=end