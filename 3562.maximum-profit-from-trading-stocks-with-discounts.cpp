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
        for (const auto& h : hierarchy) {
            children[h[0]].push_back(h[1]);
        }
        
        map<tuple<int, int, int>, int> memo;
        
        function<int(int, int, bool)> dfs = [&](int node, int remaining_budget, bool parent_bought) -> int {
            auto key = make_tuple(node, remaining_budget, parent_bought);
            if (memo.count(key)) return memo[key];
            
            int cost = parent_bought ? present[node - 1] / 2 : present[node - 1];
            int local_profit = future[node - 1] - cost;
            
            if (children[node].empty()) {
                int result = 0;
                if (cost <= remaining_budget && local_profit > 0) {
                    result = local_profit;
                }
                return memo[key] = result;
            }
            
            int num_children = children[node].size();
            
            vector<vector<int>> dp_without(num_children + 1, vector<int>(remaining_budget + 1, 0));
            for (int i = 0; i < num_children; i++) {
                int child = children[node][i];
                for (int b = 0; b <= remaining_budget; b++) {
                    dp_without[i + 1][b] = dp_without[i][b];
                    for (int b2 = 0; b2 <= b; b2++) {
                        dp_without[i + 1][b] = max(dp_without[i + 1][b], 
                                                    dp_without[i][b - b2] + dfs(child, b2, false));
                    }
                }
            }
            int max_profit = dp_without[num_children][remaining_budget];
            
            if (cost <= remaining_budget) {
                int new_budget = remaining_budget - cost;
                vector<vector<int>> dp_with(num_children + 1, vector<int>(new_budget + 1, 0));
                for (int i = 0; i < num_children; i++) {
                    int child = children[node][i];
                    for (int b = 0; b <= new_budget; b++) {
                        dp_with[i + 1][b] = dp_with[i][b];
                        for (int b2 = 0; b2 <= b; b2++) {
                            dp_with[i + 1][b] = max(dp_with[i + 1][b], 
                                                     dp_with[i][b - b2] + dfs(child, b2, true));
                        }
                    }
                }
                int total_with_buy = local_profit + dp_with[num_children][new_budget];
                max_profit = max(max_profit, total_with_buy);
            }
            
            return memo[key] = max_profit;
        };
        
        return dfs(1, budget, false);
    }
};
# @lc code=end