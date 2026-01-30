#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    // dp[u][mask] stores the max score for a subset of u's subtree with the given digit mask
    long long dp[505][1024];
    vector<int> adj[505];

    // Helper to extract a bitmask of digits for a given value; returns -1 if digits repeat
    int getMask(int val) {
        int mask = 0;
        while (val > 0) {
            int d = val % 10;
            if ((mask >> d) & 1) return -1;
            mask |= (1 << d);
            val /= 10;
        }
        return mask;
    }

    void dfs(int u, const vector<int>& vals) {
        // Initialize DP table for current node: score 0 for the empty subset
        for (int i = 0; i < 1024; ++i) dp[u][i] = -1;
        dp[u][0] = 0;

        for (int v : adj[u]) {
            dfs(v, vals);
            
            long long next_dp[1024];
            for (int i = 0; i < 1024; ++i) next_dp[i] = dp[u][i];

            // Merge child subtree results using submask iteration (O(3^10) logic)
            for (int m1 = 0; m1 < 1024; ++m1) {
                if (dp[u][m1] == -1) continue;
                int remaining = 1023 ^ m1;
                for (int m2 = remaining; m2 > 0; m2 = (m2 - 1) & remaining) {
                    if (dp[v][m2] != -1) {
                        next_dp[m1 | m2] = max(next_dp[m1 | m2], dp[u][m1] + dp[v][m2]);
                    }
                }
            }
            for (int i = 0; i < 1024; ++i) dp[u][i] = next_dp[i];
        }

        // Try including the current node 'u' in the subsets found so far
        int mask_u = getMask(vals[u]);
        if (mask_u != -1) {
            long long with_u[1024];
            for (int i = 0; i < 1024; ++i) with_u[i] = -1;

            for (int m = 0; m < 1024; ++m) {
                if (dp[u][m] != -1 && (m & mask_u) == 0) {
                    with_u[m | mask_u] = dp[u][m] + vals[u];
                }
            }
            
            for (int i = 0; i < 1024; ++i) {
                dp[u][i] = max(dp[u][i], with_u[i]);
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
        long long mod = 1e9 + 7;
        for (int i = 0; i < n; ++i) {
            long long maxS = 0;
            for (int m = 0; m < 1024; ++m) {
                maxS = max(maxS, dp[i][m]);
            }
            totalSum = (totalSum + maxS) % mod;
        }

        return (int)totalSum;
    }
};