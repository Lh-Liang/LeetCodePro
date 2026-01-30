#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.length();
        if (n < 3) return "";

        // dp[i] = minimum cost for suffix starting at i
        vector<long long> dp(n + 1, 1e15);
        dp[n] = 0;

        // Precompute prefix sums of costs for each character 'a'-'z'
        // cost_sum[char_idx][i] = sum of costs to change caption[0...i-1] to char
        vector<vector<long long>> cost_sum(26, vector<long long>(n + 1, 0));
        for (int c = 0; c < 26; ++c) {
            char target = 'a' + c;
            for (int i = 0; i < n; ++i) {
                cost_sum[c][i + 1] = cost_sum[c][i] + abs(caption[i] - target);
            }
        }

        auto get_cost = [&](int start, int end, int char_idx) {
            return cost_sum[char_idx][end] - cost_sum[char_idx][start];
        };

        // Fill DP table from right to left
        for (int i = n - 3; i >= 0; --i) {
            for (int c = 0; c < 26; ++c) {
                for (int len : {3, 4, 5}) {
                    if (i + len <= n) {
                        dp[i] = min(dp[i], get_cost(i, i + len, c) + dp[i + len]);
                    }
                }
            }
        }

        if (dp[0] >= 1e15) return "";

        // Reconstruct lexicographically smallest string
        string res = "";
        int i = 0;
        while (i < n) {
            bool found = false;
            for (int c = 0; c < 26; ++c) {
                for (int len : {3, 4, 5}) {
                    if (i + len <= n) {
                        if (get_cost(i, i + len, c) + dp[i + len] == dp[i]) {
                            res.append(len, (char)('a' + c));
                            i += len;
                            found = true;
                            break;
                        }
                    }
                }
                if (found) break;
            }
        }

        return res;
    }
};
# @lc code=end