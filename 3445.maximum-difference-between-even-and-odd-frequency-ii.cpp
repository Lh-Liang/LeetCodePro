#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    struct FenwickMin {
        int n;
        int INF;
        vector<int> bit;
        FenwickMin() : n(0), INF(1e9) {}
        FenwickMin(int n_) { init(n_); }
        void init(int n_) {
            n = n_;
            INF = 1000000000;
            bit.assign(n + 1, INF);
        }
        // point update: bit[pos] = min(bit[pos], val)
        void update(int pos, int val) {
            for (int i = pos + 1; i <= n; i += i & -i)
                bit[i] = min(bit[i], val);
        }
        // query min over [0..pos]
        int query(int pos) const {
            if (pos < 0) return INF;
            int res = INF;
            for (int i = pos + 1; i > 0; i -= i & -i)
                res = min(res, bit[i]);
            return res;
        }
    };

public:
    int maxDifference(string s, int k) {
        int n = (int)s.size();
        const int SIG = 5;

        // pref[c][i] = count of digit c in s[0..i-1]
        vector<vector<int>> pref(SIG, vector<int>(n + 1, 0));
        for (int i = 0; i < n; i++) {
            int d = s[i] - '0';
            for (int c = 0; c < SIG; c++) pref[c][i + 1] = pref[c][i];
            pref[d][i + 1]++;
        }

        int ans = INT_MIN;

        for (int a = 0; a < SIG; a++) {
            for (int b = 0; b < SIG; b++) {
                if (a == b) continue;
                int totalB = pref[b][n];
                if (totalB < 2) continue; // cannot have positive even frequency for b in any substring

                // 4 parity states: (pa%2, pb%2) => idx = (pa%2)*2 + (pb%2)
                FenwickMin fw[4];
                for (int t = 0; t < 4; t++) fw[t].init(totalB + 1);

                for (int r = k; r <= n; r++) {
                    int l = r - k;

                    // insert prefix at l
                    int pa_l = pref[a][l];
                    int pb_l = pref[b][l];
                    int pr_l = pa_l - pb_l;
                    int idx_l = ((pa_l & 1) << 1) | (pb_l & 1);
                    fw[idx_l].update(pb_l, pr_l);

                    // query for r
                    int pa_r = pref[a][r];
                    int pb_r = pref[b][r];
                    if (pb_r == 0) continue; // cannot make pb_r - pb_l > 0

                    int pr_r = pa_r - pb_r;
                    int need_pa_par = (pa_r & 1) ^ 1;
                    int need_pb_par = (pb_r & 1);
                    int idx_need = (need_pa_par << 1) | need_pb_par;

                    int bestMin = fw[idx_need].query(pb_r - 1); // enforce pb_l < pb_r
                    if (bestMin != fw[idx_need].INF) {
                        ans = max(ans, pr_r - bestMin);
                    }
                }
            }
        }

        return ans;
    }
};
// @lc code=end
