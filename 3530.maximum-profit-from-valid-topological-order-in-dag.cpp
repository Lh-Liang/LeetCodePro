#
# @lc app=leetcode id=3530 lang=cpp
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
class Solution {
public:
    int maxProfit(int n, vector<vector<int>>& edges, vector<int>& score) {
        vector<int> indeg(n, 0);
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            indeg[e[1]]++;
        }
        // Precompute prerequisites mask for each node
        vector<int> pre(n, 0);
        for (int u = 0; u < n; ++u) {
            for (int v : adj[u]) {
                pre[v] |= (1 << u);
            }
        }
        int N = 1 << n;
        vector<long long> dp(N, -1);
        dp[0] = 0;
        for (int mask = 0; mask < N; ++mask) {
            int pos = __builtin_popcount(mask) + 1;
            for (int node = 0; node < n; ++node) {
                // Only add node if all its dependencies are already placed
                if ((mask & (1 << node)) == 0 && (pre[node] & mask) == pre[node]) {
                    int new_mask = mask | (1 << node);
                    if (dp[new_mask] < dp[mask] + 1LL * score[node] * pos) {
                        dp[new_mask] = dp[mask] + 1LL * score[node] * pos;
                    }
                }
            }
        }
        // Final verification: ensure all nodes are placed and dependencies are respected
        return (int)dp[N - 1];
    }
};
# @lc code=end