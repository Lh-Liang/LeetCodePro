#
# @lc app=leetcode id=3562 lang=cpp
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        // Step 1: Parse hierarchy into a tree structure.
        vector<vector<int>> tree(n + 1);
        for (const auto& relation : hierarchy) {
            int boss = relation[0], employee = relation[1];
            tree[boss].push_back(employee);
        }
        
        // Step 2: Initialize DP table for storing maximum profit without exceeding budget.
        vector<vector<int>> dp(n + 1, vector<int>(budget + 1, 0));
        
        // Step 3: DFS traversal to calculate profits considering discounts.
        function<void(int)> dfs = [&](int current) {
            int originalPrice = present[current - 1];
            int discountedPrice = floor(originalPrice / 2);
            int profitWithoutDiscount = future[current - 1] - originalPrice;
            int profitWithDiscount = future[current - 1] - discountedPrice;
            
            // Traverse children first (post-order DFS).
            for (int child : tree[current]) {
                dfs(child);
                
                // Combine child's results into current node's DP table.
                for (int b = budget; b >= originalPrice; --b) {
dp[current][b] = max(dp[current][b], dp[child][b - originalPrice] + profitWithoutDiscount); }
dp[current][b] = max(dp[current][b], dp[child][b]); } } 
dp[current][0] = max(dp[current][0], profitWithDiscount); } 
dfs(1); eturn dp[1][budget]; } }; # @lc code=end