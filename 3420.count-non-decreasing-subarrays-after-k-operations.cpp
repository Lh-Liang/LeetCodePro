#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3420 lang=cpp
//
// [3420] Count Non-Decreasing Subarrays After K Operations
//

// @lc code=start
class Solution {
    struct Seg {
        long long v;      // prefix-max value
        int cnt;          // how many positions have this prefix-max
        long long prefCnt; // prefix sum of cnt
        long long prefSum; // prefix sum of v*cnt
    };

    struct Node {
        long long mx = 0;       // maximum in interval
        long long baseCost = 0; // cost when starting prev=0
        vector<Seg> segs;       // increasing v, with prefix sums filled

        long long costWithPrev(long long prev) const {
            if (segs.empty()) return 0;
            // find first segment with v >= prev
            auto it = lower_bound(
                segs.begin(), segs.end(), prev,
                [](const Seg& s, long long val) { return s.v < val; }
            );
            if (it == segs.begin()) return baseCost;
            int idx = int(it - segs.begin()) - 1; // last with v < prev
            long long cntBelow = segs[idx].prefCnt;
            long long sumBelow = segs[idx].prefSum;
            long long extra = prev * cntBelow - sumBelow;
            return baseCost + extra;
        }
    };

    int n;
    vector<int> a;
    vector<Node> st;

    static Node mergeNodes(const Node& L, const Node& R) {
        Node res;
        res.mx = max(L.mx, R.mx);

        long long rightCost = R.costWithPrev(L.mx);
        res.baseCost = L.baseCost + rightCost;

        res.segs.reserve(L.segs.size() + R.segs.size());
        for (const auto& s : L.segs) {
            res.segs.push_back({s.v, s.cnt, 0, 0});
        }

        long long threshold = L.mx;
        for (const auto& s : R.segs) {
            long long v2 = max(s.v, threshold);
            int c2 = s.cnt;
            if (!res.segs.empty() && res.segs.back().v == v2) {
                res.segs.back().cnt += c2;
            } else {
                res.segs.push_back({v2, c2, 0, 0});
            }
        }

        long long pc = 0, ps = 0;
        for (auto& s : res.segs) {
            pc += s.cnt;
            ps += s.v * 1LL * s.cnt;
            s.prefCnt = pc;
            s.prefSum = ps;
        }
        return res;
    }

    void build(int p, int l, int r) {
        if (l + 1 == r) {
            long long x = a[l];
            st[p].mx = x;
            st[p].baseCost = 0;
            st[p].segs = {Seg{x, 1, 1, x}};
            return;
        }
        int m = (l + r) >> 1;
        build(p << 1, l, m);
        build(p << 1 | 1, m, r);
        st[p] = mergeNodes(st[p << 1], st[p << 1 | 1]);
    }

    // Returns the first position in [idx..n] that cannot be included (i.e., boundary p).
    int walkMaxRight(int p, int l, int r, int idx, long long &prev, long long &used, long long K) {
        if (r <= idx) return idx;

        if (l >= idx) {
            long long c = st[p].costWithPrev(prev);
            if (used + c <= K) {
                used += c;
                prev = max(prev, st[p].mx);
                return r;
            }
            if (l + 1 == r) {
                return l; // cannot include this element
            }
        }

        int m = (l + r) >> 1;
        if (idx < m) {
            int leftRes = walkMaxRight(p << 1, l, m, idx, prev, used, K);
            if (leftRes < m) return leftRes;
            return walkMaxRight(p << 1 | 1, m, r, m, prev, used, K);
        } else {
            return walkMaxRight(p << 1 | 1, m, r, idx, prev, used, K);
        }
    }

public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        a = nums;
        n = (int)a.size();
        st.assign(4 * n + 5, Node());
        build(1, 0, n);

        long long K = (long long)k;
        long long ans = 0;
        for (int l = 0; l < n; l++) {
            long long prev = 0;
            long long used = 0;
            int p = walkMaxRight(1, 0, n, l, prev, used, K); // p is first not included
            ans += (long long)(p - l);
        }
        return ans;
    }
};
// @lc code=end
