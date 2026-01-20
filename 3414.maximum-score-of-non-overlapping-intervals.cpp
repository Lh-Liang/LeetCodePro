#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3414 lang=cpp
 *
 * [3414] Maximum Score of Non-overlapping Intervals
 */

// @lc code=start
class Solution {
public:
    struct State {
        long long w = 0;
        array<int, 4> idx{};
        int len = 0;
    };

    static bool lexSmaller(const State& a, const State& b) {
        int m = min(a.len, b.len);
        for (int i = 0; i < m; i++) {
            if (a.idx[i] != b.idx[i]) return a.idx[i] < b.idx[i];
        }
        return a.len < b.len;
    }

    static State better(const State& a, const State& b) {
        if (a.w != b.w) return (a.w > b.w) ? a : b;
        return lexSmaller(a, b) ? a : b;
    }

    static State addIndex(const State& base, int newIdx, long long addW) {
        State res = base;
        res.w += addW;
        // insert newIdx into sorted res.idx[0..len)
        int pos = res.len;
        while (pos > 0 && res.idx[pos - 1] > newIdx) {
            res.idx[pos] = res.idx[pos - 1];
            pos--;
        }
        res.idx[pos] = newIdx;
        res.len++;
        return res;
    }

    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = (int)intervals.size();
        struct Item {
            int l, r;
            long long w;
            int orig;
        };
        vector<Item> a;
        a.reserve(n);
        for (int i = 0; i < n; i++) {
            a.push_back({intervals[i][0], intervals[i][1], (long long)intervals[i][2], i});
        }
        sort(a.begin(), a.end(), [](const Item& x, const Item& y) {
            if (x.r != y.r) return x.r < y.r;
            if (x.l != y.l) return x.l < y.l;
            return x.orig < y.orig;
        });

        vector<int> ends(n);
        for (int i = 0; i < n; i++) ends[i] = a[i].r;

        // p[i] = number of intervals with end < a[i].l
        vector<int> p(n);
        for (int i = 0; i < n; i++) {
            p[i] = (int)(lower_bound(ends.begin(), ends.end(), a[i].l) - ends.begin());
        }

        // DP over k=0..4, i=0..n (prefix length)
        vector<State> dp_prev(n + 1), dp_cur(n + 1);
        // dp_prev is for k-1 (initially k=0 => all empty)

        for (int k = 1; k <= 4; k++) {
            dp_cur[0] = State();
            for (int i = 1; i <= n; i++) {
                // skip interval i-1
                State skip = dp_cur[i - 1];
                // take interval i-1
                int j = p[i - 1];
                State take = addIndex(dp_prev[j], a[i - 1].orig, a[i - 1].w);
                dp_cur[i] = better(skip, take);
            }
            dp_prev.swap(dp_cur);
        }

        State ans = dp_prev[n];
        vector<int> res;
        res.reserve(ans.len);
        for (int i = 0; i < ans.len; i++) res.push_back(ans.idx[i]);
        return res;
    }
};
// @lc code=end
