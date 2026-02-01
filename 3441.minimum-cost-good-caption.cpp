#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.length();
        if (n < 3) return "";

        const long long INF = 1e15;
        vector<long long> dp(n + 1, INF);
        vector<int> first_char(n + 1, 27); // Stores the char index (0-25) at dp[i]
        vector<pair<int, int>> parent(n + 1, {-1, -1}); // {char, length}

        dp[n] = 0;

        // Precompute costs to change caption[i] to character c
        vector<vector<int>> costs(26, vector<int>(n));
        for (int c = 0; c < 26; ++c) {
            for (int i = 0; i < n; ++i) {
                costs[c][i] = abs(caption[i] - (char)('a' + c));
            }
        }

        for (int i = n - 3; i >= 0; --i) {
            for (int c = 0; c < 26; ++c) {
                long long current_block_cost = (long long)costs[c][i] + costs[c][i+1] + costs[c][i+2];
                for (int len = 3; len <= 5; ++len) {
                    if (i + len > n) break;
                    if (len > 3) current_block_cost += costs[c][i + len - 1];

                    if (dp[i + len] == INF) continue;

                    long long total_cost = current_block_cost + dp[i + len];
                    bool update = false;

                    if (total_cost < dp[i]) {
                        update = true;
                    } else if (total_cost == dp[i]) {
                        // Lexicographical check
                        if (c < first_char[i]) {
                            update = true;
                        } else if (c == first_char[i]) {
                            int prev_len = parent[i].second;
                            // Compare sequence: c... (len times) + suffix(i+len) 
                            // vs c... (prev_len times) + suffix(i+prev_len)
                            if (len < prev_len) {
                                // Length 3 vs 4: compare suffix[i+3][0] with 'c'
                                if (first_char[i + len] < c) update = true;
                            } else if (len > prev_len) {
                                // Length 4 vs 3: compare 'c' with suffix[i+prev_len][0]
                                if (c < first_char[i + prev_len]) update = true;
                            }
                        }
                    }

                    if (update) {
                        dp[i] = total_cost;
                        parent[i] = {c, len};
                        first_char[i] = c;
                    }
                }
            }
        }

        if (dp[0] >= INF) return "";

        string res = "";
        int curr = 0;
        while (curr < n) {
            int c = parent[curr].first;
            int len = parent[curr].second;
            res.append(len, (char)('a' + c));
            curr += len;
        }

        return res;
    }
};
# @lc code=end