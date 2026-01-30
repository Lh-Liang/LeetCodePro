#
# @lc app=leetcode id=3615 lang=cpp
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    // dp[mask][u][v] = true if a palindromic path exists with endpoints u, v using nodes in mask
    // Using a bitset or packed array to save memory/time
    bool dp[1 << 14][14][14];

public:
    int maxLen(int n, vector<vector<int>>& edges, string label) {
        memset(dp, 0, sizeof(dp));
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        int ans = 1;

        // Base cases: length 1
        for (int i = 0; i < n; ++i) {
            dp[1 << i][i][i] = true;
        }

        // Base cases: length 2
        for (int u = 0; u < n; ++u) {
            for (int v : adj[u]) {
                if (label[u] == label[v]) {
                    dp[(1 << u) | (1 << v)][u][v] = true;
                    ans = max(ans, 2);
                }
            }
        }

        // Iterate through masks by size to ensure sub-problems are solved
        for (int mask = 1; mask < (1 << n); ++mask) {
            int len = __builtin_popcount(mask);
            if (len < 1) continue;

            for (int u = 0; u < n; ++u) {
                if (!(mask & (1 << u))) continue;
                for (int v = 0; v < n; ++v) {
                    if (!(mask & (1 << v)) || !dp[mask][u][v]) continue;

                    ans = max(ans, len);

                    // Try to expand the palindrome
                    for (int nu : adj[u]) {
                        if (mask & (1 << nu)) continue;
                        for (int nv : adj[v]) {
                            if (mask & (1 << nv)) continue;
                            if (nu == nv) continue; // Must be unique nodes
                            
                            if (label[nu] == label[nv]) {
                                int next_mask = mask | (1 << nu) | (1 << nv);
                                if (!dp[next_mask][nu][nv]) {
                                    dp[next_mask][nu][nv] = true;
                                }
                            }
                        }
                    }
                }
            }
        }

        return ans;
    }
};
# @lc code=end