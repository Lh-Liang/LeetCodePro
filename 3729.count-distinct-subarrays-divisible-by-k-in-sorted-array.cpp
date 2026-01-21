#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

class Solution {
public:
    ll gcd(ll a, ll b) {
        while (b != 0) {
            ll t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    long long numGoodSubarrays(vector<int>& nums, int k_) {
        ll K = k_;
        int n = nums.size();
        vector<ll> val, cntt;
        for (int i = 0; i < n; ) {
            ll v = nums[i];
            int j = i;
            while (j < n && nums[j] == v) ++j;
            val.push_back(v);
            cntt.push_back(j - i);
            i = j;
        }
        int m = val.size();
        if (m == 0) return 0;
        vector<ll> pre(m + 1, 0);
        for (int j = 0; j < m; ++j) {
            ll contrib = cntt[j] * (val[j] % K) % K;
            pre[j + 1] = (pre[j] + contrib) % K;
        }
        map<ll, ll> freq;
        ll ans = 0;
        for (int e = 0; e < m; ++e) {
            // multi-group ending at e
            ll ve = val[e] % K;
            ll ce = cntt[e];
            ll target = (K - pre[e]) % K;
            for (ll b = 1; b <= ce; ++b) {
                ll rmod = b * ve % K;
                ll needed = (target - rmod + K) % K;
                auto it = freq.find(needed);
                if (it != freq.end()) {
                    ans += it->second;
                }
            }
            // single group
            ll vv = val[e] % K;
            ll g = gcd(vv, K);
            ll k2 = K / g;
            ll num_single = cntt[e] / k2;
            ans += num_single;
            // add lefts from this e
            ll vs = val[e] % K;
            ll cs = cntt[e];
            ll psp1 = pre[e + 1];
            for (ll a = 1; a <= cs; ++a) {
                ll lmod = a * vs % K;
                ll effective = (lmod - psp1 + K) % K;
                ++freq[effective];
            }
        }
        return ans;
    }
};
# @lc code=end