#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3455 lang=cpp
//
// [3455] Shortest Matching Substring
//

// @lc code=start
class Solution {
    static vector<int> buildLPS(const string& pat) {
        int m = (int)pat.size();
        vector<int> lps(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && pat[i] != pat[j]) j = lps[j - 1];
            if (pat[i] == pat[j]) j++;
            lps[i] = j;
        }
        return lps;
    }

    // occ[i] = true if pat matches s starting at i. occ has size n+1.
    static vector<char> kmpOcc(const string& s, const string& pat) {
        int n = (int)s.size();
        int m = (int)pat.size();
        vector<char> occ(n + 1, 0);
        if (m == 0) {
            // Empty string matches at every position including n.
            for (int i = 0; i <= n; i++) occ[i] = 1;
            return occ;
        }
        vector<int> lps = buildLPS(pat);
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && s[i] != pat[j]) j = lps[j - 1];
            if (s[i] == pat[j]) j++;
            if (j == m) {
                int start = i - m + 1;
                occ[start] = 1;
                j = lps[j - 1];
            }
        }
        return occ;
    }

public:
    int shortestMatchingSubstring(string s, string p) {
        int n = (int)s.size();

        int star1 = (int)p.find('*');
        int star2 = (int)p.find('*', star1 + 1);
        string A = p.substr(0, star1);
        string B = p.substr(star1 + 1, star2 - star1 - 1);
        string C = p.substr(star2 + 1);

        int la = (int)A.size(), lb = (int)B.size(), lc = (int)C.size();

        auto occA = kmpOcc(s, A);
        auto occB = kmpOcc(s, B);
        auto occC = kmpOcc(s, C);

        const int INF = 1e9;
        vector<int> nextB(n + 2, INF), nextC(n + 2, INF);

        // Build nextB
        nextB[n + 1] = INF;
        for (int i = n; i >= 0; i--) {
            nextB[i] = nextB[i + 1];
            if (occB[i]) nextB[i] = i;
        }
        // Build nextC
        nextC[n + 1] = INF;
        for (int i = n; i >= 0; i--) {
            nextC[i] = nextC[i + 1];
            if (occC[i]) nextC[i] = i;
        }

        int ans = INF;
        for (int l = 0; l <= n; l++) {
            if (!occA[l]) continue;
            int x = l + la;
            if (x > n) continue;

            int m = nextB[x];
            if (m == INF) continue;
            int y = m + lb;
            if (y > n) continue;

            int cs = nextC[y];
            if (cs == INF) continue;
            int r = cs + lc;
            if (r > n) continue;

            ans = min(ans, r - l);
        }

        return (ans == INF) ? -1 : ans;
    }
};
// @lc code=end
