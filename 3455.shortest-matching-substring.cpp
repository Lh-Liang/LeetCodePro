#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static vector<int> kmpFindAll(const string& text, const string& pat) {
        int n = (int)text.size(), m = (int)pat.size();
        vector<int> res;
        if (m == 0) {
            res.reserve(n + 1);
            for (int i = 0; i <= n; ++i) res.push_back(i);
            return res;
        }
        vector<int> lps(m, 0);
        for (int i = 1, len = 0; i < m; ) {
            if (pat[i] == pat[len]) {
                lps[i++] = ++len;
            } else if (len) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
        for (int i = 0, j = 0; i < n; ) {
            if (text[i] == pat[j]) {
                ++i; ++j;
                if (j == m) {
                    res.push_back(i - m);
                    j = lps[j - 1];
                }
            } else if (j) {
                j = lps[j - 1];
            } else {
                ++i;
            }
        }
        return res;
    }

public:
    int shortestMatchingSubstring(string s, string p) {
        int n = (int)s.size();

        int i1 = (int)p.find('*');
        int i2 = (int)p.find('*', i1 + 1);
        string A = p.substr(0, i1);
        string B = p.substr(i1 + 1, i2 - (i1 + 1));
        string C = p.substr(i2 + 1);

        int la = (int)A.size(), lb = (int)B.size(), lc = (int)C.size();

        // latestAEndAt[pos] for pos in [0..n]
        vector<int> latestAEndAt(n + 1, -1);
        if (la == 0) {
            for (int pos = 0; pos <= n; ++pos) latestAEndAt[pos] = pos;
        } else {
            vector<int> bestAtEndA(n + 1, -1);
            auto matchesA = kmpFindAll(s, A);
            for (int l : matchesA) {
                int end = l + la;
                if (end <= n) bestAtEndA[end] = max(bestAtEndA[end], l);
            }
            int best = -1;
            for (int pos = 0; pos <= n; ++pos) {
                best = max(best, bestAtEndA[pos]);
                latestAEndAt[pos] = best;
            }
        }

        // bestLBefore[pos] = max l among reachable B with endB <= pos
        vector<int> bestLBefore(n + 1, -1);
        if (lb == 0) {
            // B empty occurs at every position m, endB = m; maximize l = latestAEndAt[m]
            for (int pos = 0; pos <= n; ++pos) bestLBefore[pos] = latestAEndAt[pos];
        } else {
            vector<int> bestAtEndB(n + 1, -1);
            auto matchesB = kmpFindAll(s, B);
            for (int m : matchesB) {
                int l = latestAEndAt[m];
                if (l == -1) continue;
                int endB = m + lb;
                if (endB <= n) bestAtEndB[endB] = max(bestAtEndB[endB], l);
            }
            int best = -1;
            for (int pos = 0; pos <= n; ++pos) {
                best = max(best, bestAtEndB[pos]);
                bestLBefore[pos] = best;
            }
        }

        const int INF = 1e9;
        int ans = INF;

        if (lc == 0) {
            // C empty: we can end at any position endPos
            for (int endPos = 0; endPos <= n; ++endPos) {
                int l = bestLBefore[endPos];
                if (l != -1) ans = min(ans, endPos - l);
            }
        } else {
            auto matchesC = kmpFindAll(s, C);
            for (int k : matchesC) {
                int l = bestLBefore[k];
                if (l == -1) continue;
                ans = min(ans, (k + lc) - l);
            }
        }

        return ans == INF ? -1 : ans;
    }
};
# @lc code=end
