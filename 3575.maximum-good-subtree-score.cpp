# @lc app=leetcode id=3575 lang=cpp
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
class Solution {
public:
    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        const int MOD = 1e9 + 7;
        int n = vals.size();
        vector<vector<int>> tree(n);
        // Build tree structure from parent array
        for (int i = 1; i < n; ++i) {
            tree[par[i]].push_back(i);
        }

        // Function for DFS traversal and score calculation with bitmask tracking
        function<pair<int, int>(int)> dfs = [&](int node) {
            // Get value of current node and its digit mask
            int current_value = vals[node];
            int current_mask = 0;
            for (char d : to_string(current_value)) {
                current_mask |= 1 << (d - '0');
            }
            int max_score = current_value;
            map<int, int> dp; // Store max scores for different masks
            dp[current_mask] = current_value;
            
            // Traverse children nodes of current node recursively
            for (int child : tree[node]) {
                auto [child_score, child_mask] = dfs(child);
                map<int, int> new_dp(dp);
                // Attempt combining with child results if masks do not overlap
                for (auto &[parent_mask, parent_score] : dp) {
                    if ((parent_mask & child_mask) == 0) { // Ensure unique digits constraint is maintained
                        int combined_mask = parent_mask | child_mask;
                        new_dp[combined_mask] = max(new_dp[combined_mask], parent_score + child_score);
                    }
                }
                swap(dp, new_dp); // Update dp with new combinations from this subtree level
            }

            // Determine maximum score obtainable within this subtree rooted at current node
            for (auto &[mask, score] : dp) {
                max_score = max(max_score, score);
            }

            return make_pair(max_score % MOD, current_mask);
        };
        \\ Start DFS from root node and calculate aggregate sum of maximum scores across all subtrees \\\
l long long overall_maxScore_sum = 0; \\\
l auto [score_root_0,_] = dfs(0); \\\
l overall_maxScore_sum += score_root_0; \\\
l     return overall_maxScore_sum % MOD; \@lc code=end