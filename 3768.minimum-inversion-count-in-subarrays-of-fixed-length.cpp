#include <bits/stdc++.h>
using namespace std;

#
# @lc app=leetcode id=3768 lang=cpp
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

// @lc code=start
class Solution {
    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int n = 0) { init(n); }
        void init(int n_) {
            n = n_;
            bit.assign(n + 1, 0);
        }
        void add(int i, int delta) {
            for (; i <= n; i += i & -i) bit[i] += delta;
        }
        long long sumPrefix(int i) const {
            long long s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
        long long total() const { return sumPrefix(n); }
    };

public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (k <= 1) return 0;

        // Coordinate compression
        vector<int> vals(nums.begin(), nums.end());
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int m = (int)vals.size();

        vector<int> rk(n);
        for (int i = 0; i < n; i++) {
            rk[i] = (int)(lower_bound(vals.begin(), vals.end(), nums[i]) - vals.begin()) + 1;
        }

        Fenwick fw(m);

        // Initial inversion count for first window [0..k-1]
        long long inv = 0;
        for (int i = 0; i < k; i++) {
            int x = rk[i];
            long long leq = fw.sumPrefix(x);
            long long prev = i;
            inv += (prev - leq); // previous elements greater than x
            fw.add(x, 1);
        }

        long long ans = inv;

        // Slide windows
        for (int r = k; r < n; r++) {
            int out = rk[r - k];
            // remove leftmost: subtract inversions (out, y) where y < out
            long long smaller = fw.sumPrefix(out - 1);
            inv -= smaller;
            fw.add(out, -1);

            int in = rk[r];
            // add rightmost: add inversions (y, in) where y > in
            long long greater = fw.total() - fw.sumPrefix(in);
            inv += greater;
            fw.add(in, 1);

            ans = min(ans, inv);
        }

        return ans;
    }
};
// @lc code=end
