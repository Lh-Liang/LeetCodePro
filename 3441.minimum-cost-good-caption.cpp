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

        const int INF = 1e9;
        vector<int> dp(n + 1, INF);
        vector<char> best_c(n + 1, 0);
        vector<vector<int>> SC(n + 1, vector<int>(26, INF));
        vector<vector<bool>> decision(n + 1, vector<bool>(26, false)); // false: EXTEND, true: NEW_BLOCK

        dp[n] = 0;
        for (int c = 0; c < 26; ++c) SC[n][c] = 0;

        for (int i = n - 1; i >= 0; --i) {
            // Compute dp[i] if possible
            if (i + 3 <= n) {
                for (int c = 0; c < 26; ++c) {
                    int cost3 = abs(caption[i] - (char)('a' + c)) + 
                                abs(caption[i+1] - (char)('a' + c)) + 
                                abs(caption[i+2] - (char)('a' + c));
                    int total = cost3 + SC[i+3][c];
                    if (total < dp[i]) {
                        dp[i] = total;
                        best_c[i] = (char)('a' + c);
                    } else if (total == dp[i]) {
                        if ((char)('a' + c) < best_c[i]) {
                            best_c[i] = (char)('a' + c);
                        }
                    }
                }
            }

            // Compute SC[i][c]
            for (int c = 0; c < 26; ++c) {
                int extend_cost = abs(caption[i] - (char)('a' + c)) + SC[i+1][c];
                int new_block_cost = dp[i];

                if (extend_cost < new_block_cost) {
                    SC[i][c] = extend_cost;
                    decision[i][c] = false; // EXTEND
                } else if (new_block_cost < extend_cost) {
                    SC[i][c] = new_block_cost;
                    decision[i][c] = true; // NEW_BLOCK
                } else {
                    // Tie-break: compare character at current position
                    char char_new = best_c[i];
                    char char_ext = (char)('a' + c);
                    if (char_ext <= char_new) {
                        SC[i][c] = extend_cost;
                        decision[i][c] = false;
                    } else {
                        SC[i][c] = new_block_cost;
                        decision[i][c] = true;
                    }
                }
            }
        }

        if (dp[0] >= INF) return "";

        string res = "";
        int i = 0;
        char cur = best_c[0];
        res += cur; res += cur; res += cur;
        i = 3;
        while (i < n) {
            if (decision[i][cur - 'a']) {
                cur = best_c[i];
                res += cur; res += cur; res += cur;
                i += 3;
            } else {
                res += cur;
                i += 1;
            }
        }

        return res;
    }
};
# @lc code=end