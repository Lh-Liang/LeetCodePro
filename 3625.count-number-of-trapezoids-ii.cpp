#
# @lc app=leetcode id=3625 lang=cpp
#
# [3625] Count Number of Trapezoids II
#
#include <bits/stdc++.h>
using namespace std;

# @lc code=start
class Solution {
public:
    struct SegEntry {
        int dx, dy;
        long long k;
        bool operator<(SegEntry const& other) const {
            if (dx != other.dx) return dx < other.dx;
            if (dy != other.dy) return dy < other.dy;
            return k < other.k;
        }
    };

    struct MidEntry {
        int mx, my;
        int dx, dy;
        bool operator<(MidEntry const& o) const {
            if (mx != o.mx) return mx < o.mx;
            if (my != o.my) return my < o.my;
            if (dx != o.dx) return dx < o.dx;
            return dy < o.dy;
        }
    };

    static pair<int,int> normDir(int dx, int dy) {
        if (dx == 0) {
            dy = 1;
        } else if (dy == 0) {
            dx = 1;
        } else {
            int g = std::gcd(abs(dx), abs(dy));
            dx /= g;
            dy /= g;
        }
        if (dx < 0 || (dx == 0 && dy < 0)) {
            dx = -dx;
            dy = -dy;
        }
        return {dx, dy};
    }

    int countTrapezoids(vector<vector<int>>& points) {
        int n = (int)points.size();
        long long m = 1LL * n * (n - 1) / 2;
        vector<SegEntry> segs;
        vector<MidEntry> mids;
        segs.reserve(m);
        mids.reserve(m);

        for (int i = 0; i < n; i++) {
            int xi = points[i][0], yi = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int xj = points[j][0], yj = points[j][1];
                int dx = xj - xi;
                int dy = yj - yi;
                auto [ndx, ndy] = normDir(dx, dy);

                long long k = 1LL * ndy * xi - 1LL * ndx * yi;
                segs.push_back({ndx, ndy, k});

                int mx = xi + xj;
                int my = yi + yj;
                mids.push_back({mx, my, ndx, ndy});
            }
        }

        // Step 2+3: sum over directions of sum_{lines i<j} seg_i * seg_j
        sort(segs.begin(), segs.end());
        long long totalByDirections = 0;
        int i = 0;
        while (i < (int)segs.size()) {
            int dx = segs[i].dx, dy = segs[i].dy;
            long long S = 0, sumsq = 0;
            while (i < (int)segs.size() && segs[i].dx == dx && segs[i].dy == dy) {
                long long k = segs[i].k;
                long long cnt = 0;
                while (i < (int)segs.size() && segs[i].dx == dx && segs[i].dy == dy && segs[i].k == k) {
                    cnt++;
                    i++;
                }
                S += cnt;
                sumsq += cnt * cnt;
            }
            totalByDirections += (S * S - sumsq) / 2;
        }

        // Step 5: count non-degenerate parallelograms
        sort(mids.begin(), mids.end());
        long long parallelograms = 0;
        int p = 0;
        while (p < (int)mids.size()) {
            int mx = mids[p].mx, my = mids[p].my;
            long long total = 0;
            long long degenerate = 0;
            while (p < (int)mids.size() && mids[p].mx == mx && mids[p].my == my) {
                int dx = mids[p].dx, dy = mids[p].dy;
                long long cntDir = 0;
                while (p < (int)mids.size() && mids[p].mx == mx && mids[p].my == my &&
                       mids[p].dx == dx && mids[p].dy == dy) {
                    cntDir++;
                    p++;
                }
                degenerate += cntDir * (cntDir - 1) / 2;
                total += cntDir;
            }
            parallelograms += total * (total - 1) / 2 - degenerate;
        }

        long long ans = totalByDirections - parallelograms;
        // LeetCode's template uses int; cast at the end.
        return (int)ans;
    }
};
# @lc code=end