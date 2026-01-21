#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    static constexpr long long NEG = (long long)-4e18;

    struct SegTree {
        int n;
        vector<long long> mx, lz;
        SegTree(int n=0): n(n), mx(4*n, NEG), lz(4*n, 0) {}

        void build(int idx, int l, int r, const vector<long long>& a) {
            lz[idx] = 0;
            if (l == r) {
                mx[idx] = a[l];
                return;
            }
            int m = (l + r) >> 1;
            build(idx<<1, l, m, a);
            build(idx<<1|1, m+1, r, a);
            mx[idx] = max(mx[idx<<1], mx[idx<<1|1]);
        }

        inline void apply(int idx, long long v) {
            mx[idx] += v;
            lz[idx] += v;
        }

        inline void push(int idx) {
            if (lz[idx] != 0) {
                apply(idx<<1, lz[idx]);
                apply(idx<<1|1, lz[idx]);
                lz[idx] = 0;
            }
        }

        void add(int idx, int l, int r, int ql, int qr, long long v) {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                apply(idx, v);
                return;
            }
            push(idx);
            int m = (l + r) >> 1;
            add(idx<<1, l, m, ql, qr, v);
            add(idx<<1|1, m+1, r, ql, qr, v);
            mx[idx] = max(mx[idx<<1], mx[idx<<1|1]);
        }

        long long queryMax(int idx, int l, int r, int ql, int qr) {
            if (ql > r || qr < l) return NEG;
            if (ql <= l && r <= qr) return mx[idx];
            push(idx);
            int m = (l + r) >> 1;
            return max(queryMax(idx<<1, l, m, ql, qr),
                       queryMax(idx<<1|1, m+1, r, ql, qr));
        }
    };

    long long solveRotation(const vector<int>& doubled, int start, int n, int k) {
        k = min(k, n);
        vector<long long> prev(n+1, NEG), cur(n+1, NEG);
        prev[0] = 0;

        long long best = NEG;
        // dp for exact t segments; track best over t<=k at position n
        for (int t = 1; t <= k; ++t) {
            // Build segtree over j in [0..n-1] using prev[j]
            vector<long long> base(n, NEG);
            for (int j = 0; j < n; ++j) base[j] = prev[j];

            SegTree st(n);
            st.build(1, 0, n-1, base);

            vector<pair<long long,int>> stMax; // (value, left)
            vector<pair<long long,int>> stMin; // (value, left)
            stMax.reserve(n);
            stMin.reserve(n);

            cur.assign(n+1, NEG);
            cur[0] = NEG; // cannot partition empty prefix into >=1 non-empty segments

            for (int i = 1; i <= n; ++i) {
                long long x = doubled[start + (i-1)];
                int pos = i - 1;

                // update max contributions
                int left = pos;
                while (!stMax.empty() && stMax.back().first <= x) {
                    auto [v, l] = stMax.back();
                    stMax.pop_back();
                    if (l <= left - 1) {
                        st.add(1, 0, n-1, l, left - 1, x - v);
                    }
                    left = l;
                }
                stMax.push_back({x, left});

                // update min contributions
                left = pos;
                while (!stMin.empty() && stMin.back().first >= x) {
                    auto [v, l] = stMin.back();
                    stMin.pop_back();
                    if (l <= left - 1) {
                        st.add(1, 0, n-1, l, left - 1, v - x);
                    }
                    left = l;
                }
                stMin.push_back({x, left});

                // dp transition: j in [0..i-1]
                cur[i] = st.queryMax(1, 0, n-1, 0, i-1);
            }

            best = max(best, cur[n]);
            prev.swap(cur);
        }
        return best;
    }

public:
    long long maximumScore(vector<int>& nums, int k) {
        int n = (int)nums.size();
        vector<int> doubled(2*n);
        for (int i = 0; i < 2*n; ++i) doubled[i] = nums[i % n];

        long long ans = 0; // score is always >= 0
        for (int s = 0; s < n; ++s) {
            ans = max(ans, solveRotation(doubled, s, n, k));
        }
        return ans;
    }
};
// @lc code=end
