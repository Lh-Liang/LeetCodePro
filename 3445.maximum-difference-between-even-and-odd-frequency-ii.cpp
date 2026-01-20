#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#
#include <bits/stdc++.h>
using namespace std;

# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        const int INF = 1e9;
        int n = (int)s.size();

        // prefix[d][i] = count of digit d in s[0..i)
        vector<array<int, 5>> prefix(n + 1);
        prefix[0].fill(0);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i];
            int d = s[i] - '0';
            prefix[i + 1][d]++;
        }

        auto bitUpdate = [&](vector<int>& bit, int idx, int val) {
            int m = (int)bit.size() - 1;
            for (int i = idx; i <= m; i += i & -i) bit[i] = min(bit[i], val);
        };
        auto bitQuery = [&](const vector<int>& bit, int idx) {
            int res = INF;
            for (int i = idx; i > 0; i -= i & -i) res = min(res, bit[i]);
            return res;
        };

        int ans = INT_MIN;

        for (int a = 0; a < 5; a++) {
            for (int b = 0; b < 5; b++) if (a != b) {
                int totalB = prefix[n][b];
                int m = totalB + 1; // PB values are in [0..totalB]

                // 4 BITs: paParity (0/1) x pbParity (0/1)
                vector<int> bit[2][2];
                for (int p1 = 0; p1 < 2; p1++)
                    for (int p2 = 0; p2 < 2; p2++)
                        bit[p1][p2].assign(m + 1, INF); // 1-based fenwick

                for (int r = k; r <= n; r++) {
                    int l = r - k;

                    int paL = prefix[l][a];
                    int pbL = prefix[l][b];
                    int valL = paL - pbL;
                    bitUpdate(bit[paL & 1][pbL & 1], pbL + 1, valL);

                    int paR = prefix[r][a];
                    int pbR = prefix[r][b];
                    int valR = paR - pbR;

                    int wantPa = 1 - (paR & 1);
                    int wantPb = (pbR & 1);

                    int limit = pbR - 2; // enforce PB[r] - PB[l] >= 2
                    if (limit >= 0) {
                        int minVal = bitQuery(bit[wantPa][wantPb], limit + 1);
                        if (minVal < INF) {
                            ans = max(ans, valR - minVal);
                        }
                    }
                }
            }
        }

        return ans;
    }
};
# @lc code=end
