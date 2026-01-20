#
# @lc app=leetcode id=3575 lang=cpp
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
public:
    int get_mask(int n) {
        int m = 0;
        while (n > 0) {
            int d = n % 10;
            if (m & (1 << d)) return -1;
            m |= (1 << d);
            n /= 10;
        }
        return m;
    }

    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        int n = vals.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[par[i]].push_back(i);
        }

        vector<int> masks(n);
        for (int i = 0; i < n; ++i) {
            masks[i] = get_mask(vals[i]);
        }

        // max_val_for_mask[u][m] is the max value for mask m in subtree of u
        static int max_val_for_mask[500][1024];
        memset(max_val_for_mask, 0, sizeof(max_val_for_mask));

        // Post-order traversal to fill max_val_for_mask
        // Using iterative DFS or recursion since n is small (500)
        auto fill_max_vals = [&](auto self, int u) -> void {
            if (masks[u] != -1) {
                max_val_for_mask[u][masks[u]] = vals[u];
            }
            for (int v : children[u]) {
                self(self, v);
                for (int m = 0; m < 1024; ++m) {
                    if (max_val_for_mask[v][m] > max_val_for_mask[u][m]) {
                        max_val_for_mask[u][m] = max_val_for_mask[v][m];
                    }
                }
            }
        };
        fill_max_vals(fill_max_vals, 0);

        long long total_max_score_sum = 0;
        long long MOD = 1e9 + 7;

        for (int u = 0; u < n; ++u) {
            vector<pair<int, int>> items;
            for (int m = 1; m < 1024; ++m) {
                if (max_val_for_mask[u][m] > 0) {
                    items.push_back({m, max_val_for_mask[u][m]});
                }
            }

            vector<long long> dp(1024, -1);
            dp[0] = 0;
            long long current_max = 0;

            for (auto& item : items) {
                int m_v = item.first;
                int v_v = item.second;
                for (int curr_m = 1023; curr_m >= 0; --curr_m) {
                    if (dp[curr_m] != -1 && (curr_m & m_v) == 0) {
                        int next_m = curr_m | m_v;
                        if (dp[curr_m] + v_v > dp[next_m]) {
                            dp[next_m] = dp[curr_m] + v_v;
                            if (dp[next_m] > current_max) {
                                current_max = dp[next_m];
                            }
                        }
                    }
                }
            }
            total_max_score_sum = (total_max_score_sum + current_max) % MOD;
        }

        return (int)total_max_score_sum;
    }
};
# @lc code=end