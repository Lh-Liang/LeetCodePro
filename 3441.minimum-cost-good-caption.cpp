#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.size();
        if (n < 3) return "";
        const int INF = 2000000000;
        vector<vector<vector<int>>> suff(n + 1, vector<vector<int>>(26, vector<int>(4, INF)));
        for (int c = 0; c < 26; ++c) {
            suff[n][c][3] = 0;
        }
        for (int i = n - 1; i >= 0; --i) {
            int orig = caption[i] - 'a';
            for (int pc = 0; pc < 26; ++pc) {
                for (int pk = 1; pk <= 3; ++pk) {
                    for (int d = 0; d < 26; ++d) {
                        int addc = abs(orig - d);
                        int nc, nk;
                        bool can = false;
                        if (d == pc) {
                            nc = pc;
                            nk = min(3, pk + 1);
                            can = true;
                        } else if (pk == 3) {
                            nc = d;
                            nk = 1;
                            can = true;
                        }
                        if (can) {
                            int nextc = suff[i + 1][nc][nk];
                            if (nextc < INF) {
                                suff[i][pc][pk] = min(suff[i][pc][pk], addc + nextc);
                            }
                        }
                    }
                }
            }
        }
        int min_total = INF;
        int orig0 = caption[0] - 'a';
        for (int d = 0; d < 26; ++d) {
            int addc = abs(orig0 - d);
            int nc = d;
            int nk = 1;
            int nextc = suff[1][nc][nk];
            if (nextc < INF) {
                min_total = min(min_total, addc + nextc);
            }
        }
        if (min_total == INF) return "";
        // Build the string
        string res = "";
        int pos = 0;
        int curr_c = 26;
        int curr_k = 3;
        int curr_cost = 0;
        while (pos < n) {
            int orig = caption[pos] - 'a';
            bool found = false;
            for (int d = 0; d < 26; ++d) {
                int addc = abs(orig - d);
                int nc = -1, nk = -1;
                bool can = false;
                if (d == curr_c) {
                    nc = curr_c;
                    nk = min(3, curr_k + 1);
                    can = true;
                } else if (curr_k == 3) {
                    nc = d;
                    nk = 1;
                    can = true;
                }
                if (can && suff[pos + 1][nc][nk] < INF && curr_cost + addc + suff[pos + 1][nc][nk] == min_total) {
                    res += ('a' + d);
                    curr_c = nc;
                    curr_k = nk;
                    curr_cost += addc;
                    ++pos;
                    found = true;
                    break;
                }
            }
            if (!found) return "";  // Should not happen
        }
        return res;
    }
};
# @lc code=end