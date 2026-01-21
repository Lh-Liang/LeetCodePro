#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    struct PalInfo {
        vector<int> start; // longest palindrome starting at i
        vector<int> end;   // longest palindrome ending at i
        int best;
    };

    PalInfo computePalStartEnd(const string& a) {
        int n = (int)a.size();
        vector<int> palStart(n, 1), palEnd(n, 1);
        int best = 1;

        auto expand = [&](int l, int r) {
            while (l >= 0 && r < n && a[l] == a[r]) {
                int len = r - l + 1;
                palStart[l] = max(palStart[l], len);
                palEnd[r] = max(palEnd[r], len);
                best = max(best, len);
                --l; ++r;
            }
        };

        for (int c = 0; c < n; ++c) {
            expand(c, c);     // odd
            expand(c, c + 1); // even
        }
        return {palStart, palEnd, best};
    }

    struct MatchInfo {
        vector<int> bestEndA; // best common-substring length ending at each i in A
        vector<int> bestEndB; // best common-substring length ending at each j in B
        int maxCommon;
    };

    MatchInfo commonSubstringEnds(const string& A, const string& B) {
        int n = (int)A.size(), m = (int)B.size();
        vector<int> bestEndA(n, 0), bestEndB(m, 0);
        vector<int> prev(m, 0), cur(m, 0);
        int maxCommon = 0;

        for (int i = 0; i < n; ++i) {
            fill(cur.begin(), cur.end(), 0);
            for (int j = 0; j < m; ++j) {
                if (A[i] == B[j]) {
                    cur[j] = (j ? prev[j - 1] : 0) + 1;
                    bestEndA[i] = max(bestEndA[i], cur[j]);
                    bestEndB[j] = max(bestEndB[j], cur[j]);
                    maxCommon = max(maxCommon, cur[j]);
                }
            }
            swap(prev, cur);
        }
        return {bestEndA, bestEndB, maxCommon};
    }

public:
    int longestPalindrome(string s, string t) {
        int n = (int)s.size(), m = (int)t.size();
        string rt = t;
        reverse(rt.begin(), rt.end());

        // Inside-string palindromes
        PalInfo ps = computePalStartEnd(s);
        PalInfo pt = computePalStartEnd(t);

        // Cross matching between s and reverse(t)
        MatchInfo mi = commonSubstringEnds(s, rt);
        const vector<int>& bestEndS = mi.bestEndA;
        const vector<int>& bestEndRT = mi.bestEndB;

        int ans = max(ps.best, pt.best); // taking substring from only one string

        // Pure mirrored halves (even length)
        ans = max(ans, 2 * mi.maxCommon);

        // Middle in s: palindrome starts at p, t part fully paired
        for (int p = 0; p < n; ++p) {
            int x = (p > 0 ? bestEndS[p - 1] : 0);
            ans = max(ans, ps.start[p] + 2 * x);
        }

        // Middle in t: matched part starts at r, s part fully paired
        // r in [1..m], middle palindrome ends at r-1
        for (int r = 1; r <= m; ++r) {
            int midLen = pt.end[r - 1];
            int x = 0;
            if (r < m) {
                int idxInRT = m - r - 1; // end position in rt corresponding to t[r..]
                x = bestEndRT[idxInRT];
            }
            ans = max(ans, midLen + 2 * x);
        }

        return ans;
    }
};
// @lc code=end
