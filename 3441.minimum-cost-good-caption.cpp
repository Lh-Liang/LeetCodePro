#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.length();
        if (n < 3) return "";

        // cost[i][c] is the cost to change caption[i] to character 'a' + c
        vector<vector<int>> cost(n, vector<int>(26));
        for (int i = 0; i < n; ++i) {
            for (int c = 0; c < 26; ++c) {
                cost[i][c] = abs(caption[i] - ('a' + c));
            }
        }

        // pref[c][i] is the prefix sum of costs to change characters to 'a' + c
        vector<vector<int>> pref(26, vector<int>(n + 1, 0));
        for (int c = 0; c < 26; ++c) {
            for (int i = 0; i < n; ++i) {
                pref[c][i + 1] = pref[c][i] + cost[i][c];
            }
        }

        auto get_cost = [&](int l, int r, int c) {
            return pref[c][r + 1] - pref[c][l];
        };

        const long long INF = 1e15;
        vector<long long> dp(n + 1, INF);
        vector<pair<int, int>> parent(n + 1, {-1, -1}); // {charIndex, length}

        dp[n] = 0;

        for (int i = n - 3; i >= 0; --i) {
            for (int k = 3; k <= 5; ++k) {
                if (i + k > n) break;
                for (int c = 0; c < 26; ++c) {
                    long long current_cost = (long long)get_cost(i, i + k - 1, c) + dp[i + k];
                    if (current_cost < dp[i]) {
                        dp[i] = current_cost;
                        parent[i] = {c, k};
                    } else if (current_cost == dp[i]) {
                        // Lexicographical tie-break: smaller char is better
                        if (parent[i].first == -1 || c < parent[i].first) {
                            parent[i] = {c, k};
                        }
                    }
                }
            }
        }

        if (dp[0] >= INF) return "";

        string res = "";
        int curr = 0;
        while (curr < n) {
            int c = parent[curr].first;
            int k = parent[curr].second;
            for (int j = 0; j < k; ++j) res += (char)('a' + c);
            curr += k;
        }

        return res;
    }
};
# @lc code=end