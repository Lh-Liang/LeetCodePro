#
# @lc app=leetcode id=3575 lang=cpp
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
    long long G[500][1024];
    vector<int> adj[500];
    
    int get_mask(int val) {
        int mask = 0;
        int temp = val;
        while (temp > 0) {
            int digit = temp % 10;
            if ((mask >> digit) & 1) return -1;
            mask |= (1 << digit);
            temp /= 10;
        }
        return mask;
    }

    void dfs(int u, const vector<int>& vals) {
        vector<long long> dp(1024, -1);
        dp[0] = 0;

        for (int v : adj[u]) {
            dfs(v, vals);
            vector<long long> next_dp = dp;
            for (int m1 = 0; m1 < 1024; ++m1) {
                if (dp[m1] == -1) continue;
                int rem = 1023 ^ m1;
                // Iterate over all non-empty subsets m2 of rem
                for (int m2 = rem; m2 > 0; m2 = (m2 - 1) & rem) {
                    if (G[v][m2] != -1) {
                        if (dp[m1] + G[v][m2] > next_dp[m1 | m2]) {
                            next_dp[m1 | m2] = dp[m1] + G[v][m2];
                        }
                    }
                }
            }
            dp = next_dp;
        }

        // Copy current dp to G[u]
        for (int m = 0; m < 1024; ++m) G[u][m] = dp[m];

        // Try including node u itself
        int mu = get_mask(vals[u]);
        if (mu != -1) {
            for (int m = 0; m < 1024; ++m) {
                if (dp[m] != -1 && (m & mu) == 0) {
                    if (dp[m] + vals[u] > G[u][m | mu]) {
                        G[u][m | mu] = dp[m] + vals[u];
                    }
                }
            }
        }
    }

public:
    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        int n = vals.size();
        for (int i = 0; i < n; ++i) adj[i].clear();
        for (int i = 1; i < n; ++i) {
            adj[par[i]].push_back(i);
        }

        dfs(0, vals);

        long long totalSum = 0;
        long long MOD = 1e9 + 7;

        for (int i = 0; i < n; ++i) {
            long long maxScoreU = 0;
            for (int m = 0; m < 1024; ++m) {
                if (G[i][m] > maxScoreU) maxScoreU = G[i][m];
            }
            totalSum = (totalSum + maxScoreU) % MOD;
        }

        return (int)totalSum;
    }
};
# @lc code=end