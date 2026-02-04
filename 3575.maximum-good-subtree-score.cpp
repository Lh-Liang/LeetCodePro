#
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
        // Build tree
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; ++i) {
            tree[par[i]].push_back(i);
        }
        // Helper to get digit mask
        auto get_mask = [](int x) {
            int mask = 0;
            while (x) { mask |= 1 << (x % 10); x /= 10; }
            return mask;
        };
        vector<int> val_mask(n);
        for (int i = 0; i < n; ++i) val_mask[i] = get_mask(vals[i]);
        // DP: dp[u][mask] = max sum for subtree u with used digits mask
        vector<unordered_map<int, int>> dp(n);
        vector<int> maxScore(n);

        function<void(int)> dfs = [&](int u) {
            dp[u][val_mask[u]] = vals[u];
            for (int v : tree[u]) {
                dfs(v);
                unordered_map<int, int> ndp(dp[u]);
                for (auto &[mask1, sum1] : dp[u]) {
                    for (auto &[mask2, sum2] : dp[v]) {
                        if ((mask1 & mask2) == 0) {
                            int nmask = mask1 | mask2;
                            ndp[nmask] = max(ndp[nmask], sum1 + sum2);
                        }
                    }
                }
                dp[u] = std::move(ndp);
            }
            // Find max for this node
            int best = 0;
            for (auto &[_, s] : dp[u]) best = max(best, s);
            maxScore[u] = best;
        };
        dfs(0);
        long long ans = 0;
        for (int s : maxScore) ans = (ans + s) % MOD;
        return (int)ans;
    }
};
# @lc code=end