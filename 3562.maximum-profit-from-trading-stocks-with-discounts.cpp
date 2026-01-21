#
# @lc app=leetcode id=3562 lang=cpp
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#
# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> children(n + 1);
        for (auto& edge : hierarchy) {
            children[edge[0]].push_back(edge[1]);
        }
        
        map<pair<int, int>, vector<int>> memo;
        
        function<vector<int>(int, int)> dfs = [&](int node, int parent_bought) -> vector<int> {
            auto key = make_pair(node, parent_bought);
            if (memo.count(key)) return memo[key];
            
            vector<int> dp(budget + 1, 0);
            
            // Process children first (for not buying this node)
            vector<int> children_combined(budget + 1, 0);
            for (int child : children[node]) {
                vector<int> child_dp = dfs(child, 0);
                vector<int> new_combined(budget + 1, 0);
                for (int i = 0; i <= budget; i++) {
                    for (int j = 0; j <= budget - i; j++) {
                        new_combined[i + j] = max(new_combined[i + j], children_combined[i] + child_dp[j]);
                    }
                }
                children_combined = new_combined;
            }
            
            // Option 1: Not buying this node
            dp = children_combined;
            
            // Option 2: Buying this node
            int cost = parent_bought ? present[node - 1] / 2 : present[node - 1];
            
            if (cost <= budget) {
                int node_profit = future[node - 1] - cost;
                
                // Combine node purchase with children (with discount)
                vector<int> children_combined_discounted(budget + 1, 0);
                for (int child : children[node]) {
                    vector<int> child_dp = dfs(child, 1);
                    vector<int> new_combined(budget + 1, 0);
                    for (int i = 0; i <= budget; i++) {
                        for (int j = 0; j <= budget - i; j++) {
                            new_combined[i + j] = max(new_combined[i + j], children_combined_discounted[i] + child_dp[j]);
                        }
                    }
                    children_combined_discounted = new_combined;
                }
                
                // Buy this node + children
                for (int b = 0; b <= budget - cost; b++) {
                    dp[cost + b] = max(dp[cost + b], node_profit + children_combined_discounted[b]);
                }
            }
            
            return memo[key] = dp;
        };
        
        vector<int> result = dfs(1, 0);
        return *max_element(result.begin(), result.end());
    }
};
# @lc code=end