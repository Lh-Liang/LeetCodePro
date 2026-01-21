#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#
#include <bits/stdc++.h>
using namespace std;

# @lc code=start
class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = (int)caption.size();
        const int START = 26;
        const int INF = 1e9;

        // dp indexed by (pos, prevChar in [0..26], len in [0..3])
        auto idx = [&](int pos, int prev, int len) -> int {
            return ((pos * 27 + prev) * 4 + len);
        };
        vector<int> dp((n + 1) * 27 * 4, INF);

        // base at pos == n
        for (int prev = 0; prev <= 26; ++prev) {
            for (int len = 0; len <= 3; ++len) {
                if (prev == START) {
                    dp[idx(n, prev, len)] = (len == 0 ? 0 : INF);
                } else {
                    dp[idx(n, prev, len)] = (len == 3 ? 0 : INF);
                }
            }
        }

        // fill backwards
        for (int pos = n - 1; pos >= 0; --pos) {
            int orig = caption[pos] - 'a';

            // START state only valid with len==0
            {
                int best = INF;
                for (int x = 0; x < 26; ++x) {
                    int cost = abs(orig - x);
                    int val = cost + dp[idx(pos + 1, x, 1)];
                    if (val < best) best = val;
                }
                dp[idx(pos, START, 0)] = best;
                for (int len = 1; len <= 3; ++len) dp[idx(pos, START, len)] = INF;
            }

            // normal prev chars
            for (int prev = 0; prev < 26; ++prev) {
                dp[idx(pos, prev, 0)] = INF; // invalid
                for (int len = 1; len <= 3; ++len) {
                    int best = INF;
                    for (int x = 0; x < 26; ++x) {
                        int nlen;
                        if (x == prev) {
                            nlen = (len == 3 ? 3 : len + 1);
                        } else {
                            if (len < 3) continue; // cannot switch before having 3
                            nlen = 1;
                        }
                        int cost = abs(orig - x);
                        int val = cost + dp[idx(pos + 1, x, nlen)];
                        if (val < best) best = val;
                    }
                    dp[idx(pos, prev, len)] = best;
                }
            }
        }

        if (dp[idx(0, START, 0)] >= INF) return "";

        // reconstruct lexicographically smallest among min-cost
        string ans;
        ans.reserve(n);
        int pos = 0, prev = START, len = 0;
        while (pos < n) {
            int orig = caption[pos] - 'a';
            int curBest = dp[idx(pos, prev, len)];
            bool picked = false;
            for (int x = 0; x < 26; ++x) {
                int nprev = x;
                int nlen;
                if (prev == START) {
                    nlen = 1;
                } else if (x == prev) {
                    nlen = (len == 3 ? 3 : len + 1);
                } else {
                    if (len < 3) continue;
                    nlen = 1;
                }
                int val = abs(orig - x) + dp[idx(pos + 1, nprev, nlen)];
                if (val == curBest) {
                    ans.push_back(char('a' + x));
                    prev = nprev;
                    len = nlen;
                    picked = true;
                    break;
                }
            }
            if (!picked) return ""; // should not happen
            ++pos;
        }

        return ans;
    }
};
# @lc code=end
