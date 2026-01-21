#
# @lc app=leetcode id=3327 lang=cpp
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = s.size();
        vector<vector<int>> ch(n);
        for (int i = 1; i < n; ++i) {
            ch[parent[i]].push_back(i);
        }
        for (int i = 0; i < n; ++i) {
            sort(ch[i].begin(), ch[i].end());
        }

        const long long MOD1 = 1000000007LL;
        const long long MOD2 = 1000000009LL;
        const long long B1 = 131LL;
        const long long B2 = 137LL;

        vector<long long> pow1(n + 1, 1LL);
        vector<long long> pow2(n + 1, 1LL);
        auto modmul = [](long long a, long long b, long long mod) -> long long {
            long long res = ((__int128)a * b) % mod;
            if (res < 0) res += mod;
            return res;
        };
        for (int i = 1; i <= n; ++i) {
            pow1[i] = modmul(pow1[i - 1], B1, MOD1);
            pow2[i] = modmul(pow2[i - 1], B2, MOD2);
        }

        // Iterative post-order traversal to get processing order
        vector<int> postorder;
        stack<pair<int, int>> stk;
        stk.push({0, 0});
        while (!stk.empty()) {
            auto& p = stk.top();
            int u = p.first;
            int& idx = p.second;
            if (idx == (int)ch[u].size()) {
                postorder.push_back(u);
                stk.pop();
            } else {
                int v = ch[u][idx];
                ++idx;
                stk.push({v, 0});
            }
        }

        vector<int> lens(n);
        vector<long long> fwd1(n), fwd2(n), rev1(n), rev2(n);

        for (int u : postorder) {
            long long val = (s[u] - 'a' + 1LL);

            // Forward hash
            long long h1 = 0;
            long long h2 = 0;
            int tot_len = 1;
            for (int v : ch[u]) {
                int lv = lens[v];
                h1 = (modmul(h1, pow1[lv], MOD1) + fwd1[v]) % MOD1;
                h2 = (modmul(h2, pow2[lv], MOD2) + fwd2[v]) % MOD2;
                tot_len += lv;
            }
            h1 = (modmul(h1, pow1[1], MOD1) + val) % MOD1;
            h2 = (modmul(h2, pow2[1], MOD2) + val) % MOD2;
            lens[u] = tot_len;
            fwd1[u] = h1;
            fwd2[u] = h2;

            // Reverse hash
            long long hr1 = val % MOD1;
            long long hr2 = val % MOD2;
            for (int i = (int)ch[u].size() - 1; i >= 0; --i) {
                int v = ch[u][i];
                int lv = lens[v];
                hr1 = (modmul(hr1, pow1[lv], MOD1) + rev1[v]) % MOD1;
                hr2 = (modmul(hr2, pow2[lv], MOD2) + rev2[v]) % MOD2;
            }
            rev1[u] = hr1;
            rev2[u] = hr2;
        }

        vector<bool> answer(n);
        for (int i = 0; i < n; ++i) {
            answer[i] = (fwd1[i] == rev1[i] && fwd2[i] == rev2[i]);
        }
        return answer;
    }
};
# @lc code=end
