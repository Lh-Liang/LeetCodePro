#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#

# @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        vector<int> odds, evens;
        for (int i = 1; i <= n; ++i) {
            if (i % 2) odds.push_back(i);
            else evens.push_back(i);
        }

        using ll = long long;
        // dp[pos][oddMask][evenMask][lastParity] = #ways
        unordered_map<ll, ll> memo;
        auto encode = [&](int pos, int oddMask, int evenMask, int lastParity) -> ll {
            return ((ll)pos << 40) | ((ll)oddMask << 20) | ((ll)evenMask << 1) | lastParity;
        };

        function<ll(int,int,int,int)> dp = [&](int pos, int oddMask, int evenMask, int lastParity) -> ll {
            if (pos == n) return 1;
            ll key = encode(pos, oddMask, evenMask, lastParity);
            if (memo.count(key)) return memo[key];
            ll res = 0;
            if (pos == 0) {
                // first step: can pick any
                for (int i = 0; i < odds.size(); ++i) if (!(oddMask & (1<<i))) res += dp(pos+1, oddMask|(1<<i), evenMask, 1);
                for (int i = 0; i < evens.size(); ++i) if (!(evenMask & (1<<i))) res += dp(pos+1, oddMask, evenMask|(1<<i), 0);
            } else {
                if (lastParity == 1) {
                    // last is odd, can pick an even
                    for (int i = 0; i < evens.size(); ++i) if (!(evenMask & (1<<i))) res += dp(pos+1, oddMask, evenMask|(1<<i), 0);
                } else {
                    // last is even, can pick an odd
                    for (int i = 0; i < odds.size(); ++i) if (!(oddMask & (1<<i))) res += dp(pos+1, oddMask|(1<<i), evenMask, 1);
                }
            }
            return memo[key] = res;
        };

        vector<int> ans;
        int oddMask = 0, evenMask = 0;
        int lastParity = -1;
        for (int pos = 0; pos < n; ++pos) {
            bool found = false;
            // Try all available numbers in lex order
            vector<pair<int,int>> candidates;
            if (pos == 0) {
                for (int i = 0; i < odds.size(); ++i) if (!(oddMask & (1<<i))) candidates.push_back({odds[i], 1*100 + i});
                for (int i = 0; i < evens.size(); ++i) if (!(evenMask & (1<<i))) candidates.push_back({evens[i], 0*100 + i});
            } else {
                if (lastParity == 1) {
                    for (int i = 0; i < evens.size(); ++i) if (!(evenMask & (1<<i))) candidates.push_back({evens[i], 0*100 + i});
                } else {
                    for (int i = 0; i < odds.size(); ++i) if (!(oddMask & (1<<i))) candidates.push_back({odds[i], 1*100 + i});
                }
            }
            sort(candidates.begin(), candidates.end());
            for (auto [val, code] : candidates) {
                int parity = code/100;
                int idx = code%100;
                ll cnt = 0;
                if (parity == 1) {
                    cnt = dp(pos+1, oddMask|(1<<idx), evenMask, 1);
                } else {
                    cnt = dp(pos+1, oddMask, evenMask|(1<<idx), 0);
                }
                if (k <= cnt) {
                    ans.push_back(val);
                    if (parity == 1) oddMask |= (1<<idx);
                    else evenMask |= (1<<idx);
                    lastParity = parity;
                    found = true;
                    break;
                } else {
                    k -= cnt;
                }
            }
            if (!found) return {};
        }
        return ans;
    }
};
# @lc code=end