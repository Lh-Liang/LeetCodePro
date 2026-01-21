#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        int n = coins.size();
        vector<pair<long long, int>> sorter(n);
        for (int i = 0; i < n; ++i) {
            sorter[i] = {coins[i][0], i};
        }
        sort(sorter.begin(), sorter.end());

        vector<long long> leftp(n), rightp(n), cp(n), lenp(n);
        vector<long long> pre(n + 1, 0);
        for (int ii = 0; ii < n; ++ii) {
            int i = sorter[ii].second;
            leftp[ii] = coins[i][0];
            rightp[ii] = coins[i][1];
            cp[ii] = coins[i][2];
            lenp[ii] = rightp[ii] - leftp[ii] + 1;
            pre[ii + 1] = pre[ii] + cp[ii] * lenp[ii];
        }

        auto compute_prefix = [&](long long x) -> long long {
            if (x < 1) return 0;
            auto it = lower_bound(leftp.begin(), leftp.end(), x + 1);
            int idx = it - leftp.begin();
            long long res = (idx == 0 ? 0LL : pre[idx - 1]);
            if (idx > 0) {
                long long st = leftp[idx - 1];
                if (st <= x) {
                    long long en = min(x, rightp[idx - 1]);
                    long long plen = en - st + 1;
                    res += cp[idx - 1] * plen;
                }
            }
            return res;
        };

        vector<long long> cands;
        long long kk = k;
        for (int i = 0; i < n; ++i) {
            cands.push_back(leftp[i]);
            cands.push_back(rightp[i]);
            cands.push_back(leftp[i] - kk + 1);
            cands.push_back(rightp[i] - kk + 1);
        }

        long long ans = 0;
        for (auto s : cands) {
            long long rgt = s + kk - 1;
            long long su = compute_prefix(rgt);
            long long sv = (s <= 1 ? 0LL : compute_prefix(s - 1));
            ans = max(ans, su - sv);
        }
        return ans;
    }
};
# @lc code=end