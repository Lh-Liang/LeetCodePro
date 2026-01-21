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
        const int MAX_VAL = 150;
        int m = mat.size();
        
        // dp[g] = number of ways to get GCD = g after processing current rows
        vector<long long> dp(MAX_VAL + 1, 0);
        
        // Initialize with first row
        for (int num : mat[0]) {
            dp[num] = (dp[num] + 1) % MOD;
        }
        
        // Process remaining rows
        for (int i = 1; i < m; i++) {
            vector<long long> new_dp(MAX_VAL + 1, 0);
            
            for (int num : mat[i]) {
                for (int g = 1; g <= MAX_VAL; g++) {
                    if (dp[g] > 0) {
                        int new_gcd = __gcd(g, num);
                        new_dp[new_gcd] = (new_dp[new_gcd] + dp[g]) % MOD;
                    }
                }
            }
            
            dp = new_dp;
        }
        
        return dp[1];
    }
};
# @lc code=end