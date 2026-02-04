#
# @lc app=leetcode id=3544 lang=cpp
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
class Solution {
public:
    using ll = long long;
    vector<vector<int>> tree;
    vector<int> vals;
    int K;
    // dp[node][d]: max sum for subtree rooted at node, where d is distance to nearest inverted ancestor (0<=d<k)
    vector<vector<ll>> dp;

    void dfs(int node, int parent) {
        dp[node] = vector<ll>(K, 0);
        // Base DP for leaf: value if not inverted
        dp[node][K-1] = vals[node];
        // For merging, maintain DP for both not inverting and inverting at this node
        // Merge children's DP for not inverting at this node
        for (int child : tree[node]) {
            if (child == parent) continue;
            dfs(child, node);
            vector<ll> newDp(K, LLONG_MIN);
            // For not inverting at this node: increment distance to inverted ancestor by 1
            for (int d = 1; d < K; ++d) {
                if (dp[node][d] == LLONG_MIN) continue;
                for (int cd = 0; cd < K; ++cd) {
                    if (dp[child][cd] == LLONG_MIN) continue;
                    newDp[d] = max(newDp[d], dp[node][d] + dp[child][min(cd+1,K-1)]);
                }
            }
            // For base case: d=K-1 (no inverted ancestor in range)
            for (int cd = 0; cd < K; ++cd) {
                if (dp[child][cd] == LLONG_MIN) continue;
                newDp[K-1] = max(newDp[K-1], dp[node][K-1] + dp[child][min(cd+1,K-1)]);
            }
            dp[node] = newDp;
        }
        // Try inverting at this node (only if no inverted ancestor within k)
        // When we invert, all values in this subtree (including this node) are negated
        // After inversion, the distance to an inverted ancestor resets to 0
        ll inv_sum = -vals[node];
        for (int child : tree[node]) {
            if (child == parent) continue;
            // When inverting here, children must not invert within k-1 edges (distance 0)
            inv_sum += -dp[child][0];
        }
        // Update dp[node][0] if inversion yields a better result
        dp[node][0] = max(dp[node][0], inv_sum);
    }

    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        tree.assign(n, {});
        vals = nums;
        K = k;
        for (auto& e : edges) {
            tree[e[0]].push_back(e[1]);
            tree[e[1]].push_back(e[0]);
        }
        dp.assign(n, vector<ll>(K, 0));
        dfs(0, -1);
        ll ans = LLONG_MIN;
        for (int d = 0; d < K; ++d) ans = max(ans, dp[0][d]);
        return ans;
    }
};
# @lc code=end