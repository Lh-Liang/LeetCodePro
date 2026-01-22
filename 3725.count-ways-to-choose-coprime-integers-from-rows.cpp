//
// @lc app=leetcode id=3725 lang=cpp
//
// [3725] Count Ways to Choose Coprime Integers from Rows
//

// @lc code=start
class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        const int MOD = 1e9 + 7;
        const int MAX_VAL = 151;
        
        int m = mat.size();
        
        // dp[g] = number of ways to get GCD g from previous rows
        vector<long long> dp(MAX_VAL, 0);
        
        // Process first row
        for (int v : mat[0]) {
            dp[v]++;
        }
        
        // Process remaining rows
        for (int i = 1; i < m; i++) {
            // Count frequency of each value in current row
            vector<int> freq(MAX_VAL, 0);
            for (int v : mat[i]) {
                freq[v]++;
            }
            
            vector<long long> newDp(MAX_VAL, 0);
            for (int g = 1; g < MAX_VAL; g++) {
                if (dp[g] == 0) continue;
                for (int v = 1; v < MAX_VAL; v++) {
                    if (freq[v] == 0) continue;
                    int newGcd = __gcd(g, v);
                    newDp[newGcd] = (newDp[newGcd] + dp[g] * freq[v]) % MOD;
                }
            }
            dp = newDp;
        }
        
        return (int)dp[1];
    }
};
// @lc code=end