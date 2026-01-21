#
# @lc app=leetcode id=3777 lang=cpp
#
# [3777] Minimum Deletions to Make Alternating Substring
#
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Fenwick {
    int n;
    vector<int> bit;
public:
    Fenwick(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 1, 0);
    }
    void add(int idx, int delta) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += delta;
    }
    int sumPrefix(int idx) const {
        int res = 0;
        for (; idx > 0; idx -= idx & -idx) res += bit[idx];
        return res;
    }
    int sumRange(int l, int r) const {
        if (l > r) return 0;
        return sumPrefix(r) - sumPrefix(l - 1);
    }
};

class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        int n = (int)s.size();
        Fenwick fw(max(0, n - 1)); // indices correspond to i=1..n-1

        auto eq = [&](int i) -> int {
            // e[i] where i in [1..n-1]
            return (s[i] == s[i - 1]) ? 1 : 0;
        };

        for (int i = 1; i < n; i++) {
            fw.add(i, eq(i));
        }

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto &qu : queries) {
            if (qu[0] == 1) {
                int j = qu[1];

                int old1 = 0, old2 = 0;
                if (j > 0) old1 = (s[j] == s[j - 1]);
                if (j + 1 < n) old2 = (s[j + 1] == s[j]);

                // flip
                s[j] = (s[j] == 'A') ? 'B' : 'A';

                int new1 = 0, new2 = 0;
                if (j > 0) new1 = (s[j] == s[j - 1]);
                if (j + 1 < n) new2 = (s[j + 1] == s[j]);

                if (j > 0) fw.add(j, new1 - old1);
                if (j + 1 < n) fw.add(j + 1, new2 - old2);
            } else {
                int l = qu[1], r = qu[2];
                if (l == r) {
                    ans.push_back(0);
                } else {
                    // sum e[i] for i in [l+1, r]
                    ans.push_back(fw.sumRange(l + 1, r));
                }
            }
        }
        return ans;
    }
};
// @lc code=end
