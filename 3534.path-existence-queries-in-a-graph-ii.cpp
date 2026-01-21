#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        int D = maxDiff;
        vector<pair<int,int>> a;
        a.reserve(n);
        for (int i = 0; i < n; ++i) a.push_back({nums[i], i});
        sort(a.begin(), a.end());

        vector<int> val(n), pos(n);
        for (int i = 0; i < n; ++i) {
            val[i] = a[i].first;
            pos[a[i].second] = i;
        }

        // next[i]: farthest right index reachable in 1 step from i
        vector<int> nxt(n);
        int r = 0;
        for (int i = 0; i < n; ++i) {
            if (r < i) r = i;
            while (r + 1 < n && val[r + 1] <= val[i] + D) ++r;
            nxt[i] = r;
        }

        // prev[i]: farthest left index reachable in 1 step from i
        vector<int> prv(n);
        int l = 0;
        for (int i = 0; i < n; ++i) {
            while (val[i] - val[l] > D) ++l;
            prv[i] = l;
        }

        int LOG = 1;
        while ((1 << LOG) <= n) ++LOG;

        vector<vector<int>> jumpR(LOG, vector<int>(n));
        vector<vector<int>> jumpL(LOG, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            jumpR[0][i] = nxt[i];
            jumpL[0][i] = prv[i];
        }
        for (int k = 1; k < LOG; ++k) {
            for (int i = 0; i < n; ++i) {
                jumpR[k][i] = jumpR[k-1][ jumpR[k-1][i] ];
                jumpL[k][i] = jumpL[k-1][ jumpL[k-1][i] ];
            }
        }

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto &q : queries) {
            int u = q[0], v = q[1];
            int su = pos[u], sv = pos[v];
            if (su == sv) {
                ans.push_back(0);
                continue;
            }

            long long steps = 0;
            if (su < sv) {
                int cur = su;
                for (int k = LOG - 1; k >= 0; --k) {
                    int cand = jumpR[k][cur];
                    if (cand < sv && cand != cur) {
                        cur = cand;
                        steps += 1LL << k;
                    }
                }
                // one more step?
                if (jumpR[0][cur] >= sv) ans.push_back((int)(steps + 1));
                else ans.push_back(-1);
            } else {
                int cur = su;
                for (int k = LOG - 1; k >= 0; --k) {
                    int cand = jumpL[k][cur];
                    if (cand > sv && cand != cur) {
                        cur = cand;
                        steps += 1LL << k;
                    }
                }
                if (jumpL[0][cur] <= sv) ans.push_back((int)(steps + 1));
                else ans.push_back(-1);
            }
        }

        return ans;
    }
};
// @lc code=end
