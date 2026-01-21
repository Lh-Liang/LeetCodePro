#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3327 lang=cpp
//
// [3327] Check if DFS Strings Are Palindromes
//

// @lc code=start
class Solution {
public:
    static constexpr int MOD1 = 1000000007;
    static constexpr int MOD2 = 1000000009;
    static constexpr int BASE = 911382323; // < both MODs

    static inline int addmod(long long a, int mod) {
        a %= mod;
        if (a < 0) a += mod;
        return (int)a;
    }

    pair<int,int> getHash(const vector<int>& pref1, const vector<int>& pref2,
                          const vector<int>& pow1, const vector<int>& pow2,
                          int l, int r) {
        // inclusive [l, r]
        long long x1 = pref1[r+1] - (long long)pref1[l] * pow1[r-l+1];
        long long x2 = pref2[r+1] - (long long)pref2[l] * pow2[r-l+1];
        return {addmod(x1, MOD1), addmod(x2, MOD2)};
    }

    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = (int)parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) {
            children[parent[i]].push_back(i);
        }
        // children lists are already in increasing order because i increases.

        // Iterative postorder traversal from root 0.
        vector<int> it(n, 0);
        vector<int> st;
        st.reserve(n);
        st.push_back(0);

        vector<int> sz(n, 0), L(n, 0), R(n, 0);
        string post;
        post.reserve(n);

        while (!st.empty()) {
            int x = st.back();
            if (it[x] < (int)children[x].size()) {
                int y = children[x][it[x]++];
                st.push_back(y);
            } else {
                st.pop_back();

                int pos = (int)post.size();
                post.push_back(s[x]);

                int subtotal = 1;
                for (int y : children[x]) subtotal += sz[y];
                sz[x] = subtotal;

                R[x] = pos;
                L[x] = pos - sz[x] + 1;
            }
        }

        // Build rolling hashes for post and reversed(post)
        string rev = post;
        reverse(rev.begin(), rev.end());

        vector<int> pow1(n+1, 1), pow2(n+1, 1);
        for (int i = 1; i <= n; i++) {
            pow1[i] = (long long)pow1[i-1] * BASE % MOD1;
            pow2[i] = (long long)pow2[i-1] * BASE % MOD2;
        }

        vector<int> pref1(n+1, 0), pref2(n+1, 0);
        vector<int> rpref1(n+1, 0), rpref2(n+1, 0);
        for (int i = 0; i < n; i++) {
            int v1 = (post[i] - 'a' + 1);
            pref1[i+1] = ((long long)pref1[i] * BASE + v1) % MOD1;
            pref2[i+1] = ((long long)pref2[i] * BASE + v1) % MOD2;

            int v2 = (rev[i] - 'a' + 1);
            rpref1[i+1] = ((long long)rpref1[i] * BASE + v2) % MOD1;
            rpref2[i+1] = ((long long)rpref2[i] * BASE + v2) % MOD2;
        }

        vector<bool> ans(n, false);
        for (int i = 0; i < n; i++) {
            int l = L[i], r = R[i];
            auto hF = getHash(pref1, pref2, pow1, pow2, l, r);
            int rl = n - 1 - r;
            int rr = n - 1 - l;
            auto hR = getHash(rpref1, rpref2, pow1, pow2, rl, rr);
            ans[i] = (hF == hR);
        }
        return ans;
    }
};
// @lc code=end
