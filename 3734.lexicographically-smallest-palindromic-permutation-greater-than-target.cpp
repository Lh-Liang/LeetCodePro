#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = (int)s.size();
        vector<int> cnt(26, 0);
        for (char ch : s) cnt[ch - 'a']++;

        int odd = 0, midIdx = -1;
        for (int c = 0; c < 26; c++) {
            if (cnt[c] % 2) {
                odd++;
                midIdx = c;
            }
        }
        if (odd > 1) return "";
        if (n % 2 == 0) {
            if (odd != 0) return "";
        } else {
            // total length is odd => must have exactly one odd count
            if (odd != 1) return "";
        }

        string mid;
        if (midIdx != -1) mid.push_back(char('a' + midIdx));

        int m = n / 2;
        vector<int> half(26, 0);
        for (int c = 0; c < 26; c++) half[c] = cnt[c] / 2;

        string A = target.substr(0, m);

        // Check if A itself can be the left half.
        {
            vector<int> cntA(26, 0);
            for (char ch : A) cntA[ch - 'a']++;
            bool ok = true;
            for (int c = 0; c < 26; c++) {
                if (cntA[c] != half[c]) { ok = false; break; }
            }
            if (ok) {
                string rev = A;
                reverse(rev.begin(), rev.end());
                string P0 = A + mid + rev;
                if (P0 > target) return P0;
            }
        }

        // Precompute prefix counts of A.
        vector<array<int, 26>> pref(m + 1);
        pref[0].fill(0);
        for (int i = 0; i < m; i++) {
            pref[i + 1] = pref[i];
            pref[i + 1][A[i] - 'a']++;
        }

        auto prefixFeasible = [&](int p) -> bool {
            for (int c = 0; c < 26; c++) {
                if (pref[p][c] > half[c]) return false;
            }
            return true;
        };

        // Find the smallest multiset permutation H such that H > A.
        for (int p = m - 1; p >= 0; --p) {
            if (!prefixFeasible(p)) continue;

            array<int, 26> rem;
            for (int c = 0; c < 26; c++) rem[c] = half[c] - pref[p][c];

            int a = A[p] - 'a';
            for (int d = a + 1; d < 26; d++) {
                if (rem[d] == 0) continue;

                rem[d]--;
                int L = m - p - 1;
                string suf;
                suf.reserve(L);
                for (int c = 0; c < 26; c++) {
                    if (rem[c] > 0) suf.append(rem[c], char('a' + c));
                }

                string H = A.substr(0, p);
                H.push_back(char('a' + d));
                H += suf;

                string rev = H;
                reverse(rev.begin(), rev.end());
                return H + mid + rev;
            }
        }

        return "";
    }
};
# @lc code=end
