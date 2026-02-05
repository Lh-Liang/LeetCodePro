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
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[par[i]].push_back(i);
        }
        // Helper to get the digit bitmask of a single value
        auto get_mask = [](int val) {
            int mask = 0;
            while (val > 0) {
                mask |= (1 << (val % 10));
                val /= 10;
            }
            return mask;
        };
        // DP[u]: map from digit bitmask to max sum in subtree u
        vector<unordered_map<int, int>> DP(n);
        function<void(int)> dfs = [&](int u) {
            int my_mask = get_mask(vals[u]);
            DP[u][my_mask] = vals[u];
            for (int v : children[u]) {
                dfs(v);
                unordered_map<int, int> new_dp = DP[u];
                for (auto &[mask1, sum1] : DP[u]) {
                    for (auto &[mask2, sum2] : DP[v]) {
                        if ((mask1 & mask2) == 0) {
                            int comb_mask = mask1 | mask2;
                            new_dp[comb_mask] = max(new_dp[comb_mask], sum1 + sum2);
                        }
                    }
                }
                DP[u] = move(new_dp);
            }
        };
        dfs(0);
        // For each node, collect its maximal DP value and sum
        int ans = 0;
        for (int u = 0; u < n; ++u) {
            int local_max = 0;
            for (auto &p : DP[u]) local_max = max(local_max, p.second);
            ans = (ans + local_max) % MOD;
        }
        return ans;
    }
};
# @lc code=end