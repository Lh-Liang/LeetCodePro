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
        
        // dp[node][d][p] = max sum from subtree of node
        // d = distance from nearest inverted ancestor (k means >= k, can invert)
        // p = parity of inversions (0 = even, 1 = odd)
        vector<vector<vector<long long>>> dp(n, vector<vector<long long>>(k + 1, vector<long long>(2, 0)));
        
        vector<int> parent(n, -1);
        vector<int> order;
        queue<int> q;
        vector<bool> visited(n, false);
        
        q.push(0);
        visited[0] = true;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    parent[v] = u;
                    q.push(v);
                }
            }
        }
        
        // Reverse to process children before parents
        reverse(order.begin(), order.end());
        
        for (int u : order) {
            int par = parent[u];
            for (int d = 0; d <= k; d++) {
                for (int p = 0; p <= 1; p++) {
                    long long val = (p == 0) ? (long long)nums[u] : -(long long)nums[u];
                    
                    if (d < k) {
                        // Cannot invert at this node
                        long long sum = val;
                        for (int v : adj[u]) {
                            if (v == par) continue;
                            sum += dp[v][min(d + 1, k)][p];
                        }
                        dp[u][d][p] = sum;
                    } else {
                        // Can choose to invert or not
                        long long noInvert = val;
                        for (int v : adj[u]) {
                            if (v == par) continue;
                            noInvert += dp[v][k][p];
                        }
                        
                        long long doInvert = -val;
                        for (int v : adj[u]) {
                            if (v == par) continue;
                            doInvert += dp[v][1][1 - p];
                        }
                        
                        dp[u][d][p] = max(noInvert, doInvert);
                    }
                }
            }
        }
        
        return dp[0][k][0];
    }
};
# @lc code=end