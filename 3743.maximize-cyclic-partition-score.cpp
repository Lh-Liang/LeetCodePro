#
# @lc app=leetcode id=3743 lang=cpp
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ext(2 * n);
        for (int i = 0; i < 2 * n; ++i) {
            ext[i] = nums[i % n];
        }
        int N = 2 * n;
        int LOG = 0;
        while ((1 << LOG) <= N) ++LOG;
        vector<vector<int>> spmax(LOG, vector<int>(N));
        vector<vector<int>> spmin(LOG, vector<int>(N));
        for (int i = 0; i < N; ++i) {
            spmax[0][i] = spmin[0][i] = ext[i];
        }
        for (int lv = 1; lv < LOG; ++lv) {
            for (int i = 0; i + (1 << lv) <= N; ++i) {
                spmax[lv][i] = max(spmax[lv - 1][i], spmax[lv - 1][i + (1 << (lv - 1))]);
                spmin[lv][i] = min(spmin[lv - 1][i], spmin[lv - 1][i + (1 << (lv - 1))]);
            }
        }
        auto get_max = [&](int L, int R) -> int {
            int leng = R - L + 1;
            int lg = 31 - __builtin_clz(leng);
            return max(spmax[lg][L], spmax[lg][R - (1 << lg) + 1]);
        };
        auto get_min = [&](int L, int R) -> int {
            int leng = R - L + 1;
            int lg = 31 - __builtin_clz(leng);
            return min(spmin[lg][L], spmin[lg][R - (1 << lg) + 1]);
        };
        long long ans = 0;
        vector<long long> dpa(n + 1);
        vector<long long> dpb(n + 1);
        for (int s = 0; s < n; ++s) {
            fill(dpa.begin(), dpa.end(), LLONG_MIN / 2);
            dpa[0] = 0;
            vector<long long>* now = &dpa;
            vector<long long>* nxtt = &dpb;
            for (int p = 1; p <= k; ++p) {
                int optt = p - 1;
                for (int len = p; len <= n; ++len) {
                    long long best = LLONG_MIN / 2;
                    int start_pr = optt;
                    for (int pr = start_pr; pr < len; ++pr) {
                        long long cc = (long long)get_max(s + pr, s + len - 1) - get_min(s + pr, s + len - 1);
                        long long temp = (*now)[pr] + cc;
                        if (temp > best) {
                            best = temp;
                            optt = pr;
                        }
                    }
                    (*nxtt)[len] = best;
                }
                auto* tmp = now;
                now = nxtt;
                nxtt = tmp;
            }
            ans = max(ans, (*now)[n]);
        }
        return ans;
    }
};
# @lc code=end