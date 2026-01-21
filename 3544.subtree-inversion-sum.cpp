#
# @lc app=leetcode id=3544 lang=cpp
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<vector<int>> children(n);
        function<void(int, int)> build = [&](int u, int p) {
            for (int v : adj[u]) {
                if (v != p) {
                    children[u].push_back(v);
                    build(v, u);
                }
            }
        };
        build(0, -1);

        int K = k;
        vector<vector<vector<long long>>> dp(n, vector<vector<long long>>(2, vector<long long>(K, LLONG_MIN / 2)));

        function<void(int)> compute = [&](int u) {
            for (int v : children[u]) {
                compute(v);
            }
            for (int p = 0; p < 2; ++p) {
                for (int s = 0; s < K; ++s) {
                    // x = 0 always possible
                    {
                        int x = 0;
                        long long contrib = nums[u] * (((p + x) % 2 == 0) ? 1LL : -1LL);
                        int new_p = (p + x) % 2;
                        int new_s;
                        if (x == 1) {
                            int ndist = 1;
                            new_s = (ndist >= K ? 0 : ndist);
                        } else {
                            if (s == 0) {
                                new_s = 0;
                            } else {
                                int ndist = s + 1;
                                new_s = (ndist >= K ? 0 : ndist);
                            }
                        }
                        long long sub = 0;
                        for (int v : children[u]) {
                            sub += dp[v][new_p][new_s];
                        }
                        dp[u][p][s] = contrib + sub;
                    }
                    // x = 1 if allowed
                    if (s == 0) {
                        int x = 1;
                        long long contrib = nums[u] * (((p + x) % 2 == 0) ? 1LL : -1LL);
                        int new_p = (p + x) % 2;
                        int new_s;
                        {
                            int ndist = 1;
                            new_s = (ndist >= K ? 0 : ndist);
                        }
                        long long sub = 0;
                        for (int v : children[u]) {
                            sub += dp[v][new_p][new_s];
                        }
                        long long candidate = contrib + sub;
                        if (candidate > dp[u][p][s]) {
                            dp[u][p][s] = candidate;
                        }
                    }
                }
            }
        };
        compute(0);
        return dp[0][0][0];
    }
};
# @lc code=end