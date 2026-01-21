#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int shortestMatchingSubstring(string s, string p) {
        size_t star1 = p.find('*');
        size_t star2 = p.find('*', star1 + 1);
        string A = p.substr(0, star1);
        string B = p.substr(star1 + 1, star2 - star1 - 1);
        string C = p.substr(star2 + 1);
        int lenA = A.length();
        int lenB = B.length();
        int lenC = C.length();
        int n = s.length();

        auto get_matches = [&](const string& text, const string& pat) -> vector<int> {
            int tn = text.length();
            int m = pat.length();
            if (m == 0) {
                vector<int> res(tn + 1);
                iota(res.begin(), res.end(), 0);
                return res;
            }
            vector<int> pi(m, 0);
            for (int i = 1, j = 0; i < m; ++i) {
                while (j && pat[i] != pat[j]) j = pi[j - 1];
                if (pat[i] == pat[j]) ++j;
                pi[i] = j;
            }
            vector<int> res;
            int q = 0;
            for (int i = 0; i < tn; ++i) {
                while (q && text[i] != pat[q]) q = pi[q - 1];
                if (text[i] == pat[q]) ++q;
                if (q == m) {
                    res.push_back(i - m + 1);
                    q = pi[q - 1];
                }
            }
            return res;
        };

        vector<int> posA = get_matches(s, A);
        vector<int> posB = get_matches(s, B);
        vector<int> posC = get_matches(s, C);

        int ans = INT_MAX;
        for (int j : posB) {
            int upper = j - lenA;
            if (upper < 0) continue;
            auto it = upper_bound(posA.begin(), posA.end(), upper);
            if (it == posA.begin()) continue;
            --it;
            int i = *it;
            int lower_k = j + lenB;
            auto it2 = lower_bound(posC.begin(), posC.end(), lower_k);
            if (it2 == posC.end()) continue;
            int k = *it2;
            int length = k + lenC - i;
            if (length < ans) ans = length;
        }
        return ans == INT_MAX ? -1 : ans;
    }
};
# @lc code=end