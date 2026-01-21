#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.size();
        vector<vector<int>> prefix(5, vector<int>(n + 1, 0));
        vector<vector<int>> parity(5, vector<int>(n + 1, 0));
        for (int i = 1; i <= n; ++i) {
            int ch = s[i - 1] - '0';
            for (int c = 0; c < 5; ++c) {
                prefix[c][i] = prefix[c][i - 1] + (c == ch);
                parity[c][i] = prefix[c][i] % 2;
            }
        }
        const int INF = 2000000000;
        const int MAXP = 30010;
        int ans = -INF;
        for (int a = 0; a < 5; ++a) {
            for (int b = 0; b < 5; ++b) {
                if (a == b) continue;
                vector<int> diff(n + 1);
                for (int t = 0; t <= n; ++t) {
                    diff[t] = prefix[a][t] - prefix[b][t];
                }
                auto update = [&](vector<int>& tree, int idx, int val) {
                    for (; idx <= MAXP; idx += idx & -idx) {
                        tree[idx] = min(tree[idx], val);
                    }
                };
                auto query = [&](const vector<int>& tree, int idx) -> int {
                    int res = INF;
                    for (; idx > 0; idx -= idx & -idx) {
                        res = min(res, tree[idx]);
                    }
                    return res;
                };
                vector<vector<int>> trees(4, vector<int>(MAXP + 1, INF));
                int left = 0;
                for (int t = 1; t <= n; ++t) {
                    int maxstart = t - k;
                    while (left <= maxstart && left <= n) {
                        int pAu = parity[a][left];
                        int pBu = parity[b][left];
                        int state = pAu * 2 + pBu;
                        int pbu = prefix[b][left];
                        update(trees[state], pbu + 1, diff[left]);
                        ++left;
                    }
                    int pAt = parity[a][t];
                    int pBt = parity[b][t];
                    int target_pa = 1 - pAt;
                    int target_state = target_pa * 2 + pBt;
                    int M = prefix[b][t] - 2;
                    if (M < 0) continue;
                    int min_d = query(trees[target_state], M + 1);
                    if (min_d == INF) continue;
                    ans = max(ans, diff[t] - min_d);
                }
            }
        }
        return ans == -INF ? -1 : ans;
    }
};
# @lc code=end