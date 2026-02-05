#
# @lc app=leetcode id=3544 lang=cpp
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
class Solution {
public:
    typedef long long ll;
    vector<vector<int>> tree;
    int K;
    vector<vector<ll>> dfs(int u, int parent, const vector<int>& nums) {
        // dp[d]: max sum if the closest inversion among ancestors is d edges away (0 <= d <= K)
        vector<vector<ll>> childDPs;
        for (int v : tree[u]) {
            if (v == parent) continue;
            childDPs.push_back(dfs(v, u, nums));
        }
        // dp0: not inverting at this node
        // dp1: inverting at this node (if allowed)
        vector<ll> dp0(K+2, 0), dp1(K+2, 0);
        // Base cases
        dp0[0] = nums[u];
        dp1[0] = -nums[u];
        for (auto& cdp : childDPs) {
            vector<ll> newDp0(K+2, LLONG_MIN/2), newDp1(K+2, LLONG_MIN/2);
            // Merge for not inverting here: increment ancestor inversion distance for children
            for (int d = 0; d <= K; ++d) {
                for (int cd = 0; cd <= K; ++cd) {
                    if (dp0[d] == LLONG_MIN/2 || cdp[cd] == LLONG_MIN/2) continue;
                    int nd = min(d, cd+1);
                    newDp0[nd] = max(newDp0[nd], dp0[d] + cdp[cd]);
                }
            }
            swap(dp0, newDp0);
        }
        // Case: invert at this node (if ancestor inversion at least k away)
        // Only possible if ancestor inversion distance >= K
        for (int d = 0; d <= K; ++d) {
            if (d < K) dp1[d] = LLONG_MIN/2;
        }
        for (auto& cdp : childDPs) {
            vector<ll> newDp1(K+2, LLONG_MIN/2);
            for (int d = 0; d <= K; ++d) {
                for (int cd = 0; cd <= K; ++cd) {
                    if (dp1[d] == LLONG_MIN/2 || cdp[cd] == LLONG_MIN/2) continue;
                    int nd = min(d, cd+1);
                    newDp1[nd] = max(newDp1[nd], dp1[d] + cdp[cd]);
                }
            }
            swap(dp1, newDp1);
        }
        // Now, if we invert at this node, must flip whole subtree
        for (int d = 0; d <= K; ++d) {
            dp1[d] = dp1[d];
        }
        // Compose final dp for this node:
        vector<ll> dp(K+2, LLONG_MIN/2);
        for (int d = 0; d <= K; ++d)
            dp[d] = max(dp0[d], dp1[d]);
        return {dp};
    }
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        tree.assign(n, {});
        K = k;
        for (auto& e : edges) {
            tree[e[0]].push_back(e[1]);
            tree[e[1]].push_back(e[0]);
        }
        auto dp = dfs(0, -1, nums)[0];
        ll res = LLONG_MIN;
        for (int d = 0; d <= K; ++d) res = max(res, dp[d]);
        return res;
    }
};
# @lc code=end