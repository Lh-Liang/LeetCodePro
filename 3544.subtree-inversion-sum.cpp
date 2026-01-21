#
# @lc app=leetcode id=3544 lang=cpp
#
# [3544] Subtree Inversion Sum
#
# @lc code=start
class Solution {
public:
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        // Build tree structure
        vector<vector<int>> children(n);
        function<void(int, int)> build = [&](int u, int parent) {
            for (int v : adj[u]) {
                if (v != parent) {
                    children[u].push_back(v);
                    build(v, u);
                }
            }
        };
        build(0, -1);
        
        // dp[u][d][parity]
        vector<vector<vector<long long>>> dp(n, vector<vector<long long>>(k+1, vector<long long>(2, LLONG_MIN)));
        vector<vector<vector<bool>>> computed(n, vector<vector<bool>>(k+1, vector<bool>(2, false)));
        
        function<long long(int, int, int)> solve = [&](int u, int dist, int parity) -> long long {
            if (computed[u][dist][parity]) return dp[u][dist][parity];
            computed[u][dist][parity] = true;
            
            long long current_val = (parity == 0) ? nums[u] : -nums[u];
            
            // Option 1: Don't invert u
            long long sum1 = current_val;
            for (int v : children[u]) {
                int next_dist = min(dist + 1, k);
                sum1 += solve(v, next_dist, parity);
            }
            long long result = sum1;
            
            // Option 2: Invert u (only if dist >= k)
            if (dist >= k) {
                long long sum2 = -current_val;
                for (int v : children[u]) {
                    sum2 += solve(v, 1, 1 - parity);
                }
                result = max(result, sum2);
            }
            
            dp[u][dist][parity] = result;
            return result;
        };
        
        return solve(0, k, 0);
    }
};
# @lc code=end