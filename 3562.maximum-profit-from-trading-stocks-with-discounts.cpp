# @lc app=leetcode id=3562 lang=cpp
# [3562] Maximum Profit from Trading Stocks with Discounts

# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        // Step 1: Initialize profits and discounted prices arrays
        vector<int> profits(n);
        vector<int> discountedPrices = present;
        
        // Step 2: Calculate base profits without discounts
        for (int i = 0; i < n; ++i) {
            profits[i] = future[i] - present[i];
        }
        
        // Step 3: Apply discounts based on hierarchy
        for (const auto& pair : hierarchy) {
            int boss = pair[0] - 1;
            int employee = pair[1] - 1;
            discountedPrices[employee] = min(discountedPrices[employee], present[employee] / 2);
        }
        
        // Step 4: Use dynamic programming or greedy to maximize profit under the budget constraint
        vector<vector<int>> dp(n + 1, vector<int>(budget + 1, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = budget; j >= discountedPrices[i]; --j) {
                dp[i + 1][j] = max(dp[i][j], dp[i][j - discountedPrices[i]] + profits[i]);
            }
            for (int j = discountedPrices[i] - 1; j >= 0; --j) {
                dp[i + 1][j] = dp[i][j];
            }
        }
        
        // Step 5: Return maximum profit achievable within the budget
        return dp[n][budget];
    }
};
# @lc code=end