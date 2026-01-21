#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3762 lang=cpp
//
// [3762] Minimum Operations to Equalize Subarrays
//

// @lc code=start
class Solution {
    struct WaveletTree {
        int lo, hi;
        WaveletTree *l = nullptr, *r = nullptr;
        vector<int> b;              // prefix count going to left
        vector<long long> sLeft;    // prefix sum of values going to left
        vector<long long> prefAll;  // prefix sum of all values at this node

        WaveletTree(const vector<int>& arr, int _lo, int _hi) : lo(_lo), hi(_hi) {
            int n = (int)arr.size();
            b.assign(n + 1, 0);
            sLeft.assign(n + 1, 0);
            prefAll.assign(n + 1, 0);
            if (n == 0) return;
            if (lo == hi) {
                for (int i = 0; i < n; i++) {
                    prefAll[i + 1] = prefAll[i] + arr[i];
                }
                return;
            }
            int mid = lo + (hi - lo) / 2;
            vector<int> leftArr; leftArr.reserve(n);
            vector<int> rightArr; rightArr.reserve(n);

            for (int i = 0; i < n; i++) {
                int x = arr[i];
                prefAll[i + 1] = prefAll[i] + x;
                if (x <= mid) {
                    leftArr.push_back(x);
                    b[i + 1] = b[i] + 1;
                    sLeft[i + 1] = sLeft[i] + x;
                } else {
                    rightArr.push_back(x);
                    b[i + 1] = b[i];
                    sLeft[i + 1] = sLeft[i];
                }
            }

            if (!leftArr.empty()) l = new WaveletTree(leftArr, lo, mid);
            if (!rightArr.empty()) r = new WaveletTree(rightArr, mid + 1, hi);
        }

        ~WaveletTree() {
            delete l;
            delete r;
        }

        // kth smallest in positions [L,R] (1-indexed), k is 1-indexed
        int kth(int L, int R, int k) const {
            if (L > R) return 0;
            if (lo == hi) return lo;
            int inLeft = b[R] - b[L - 1];
            if (k <= inLeft) {
                if (!l) return lo; // should not happen if counts consistent
                int nL = b[L - 1] + 1;
                int nR = b[R];
                return l->kth(nL, nR, k);
            } else {
                if (!r) return hi;
                int nL = L - b[L - 1];
                int nR = R - b[R];
                return r->kth(nL, nR, k - inLeft);
            }
        }

        // returns {count, sum} of values <= x in positions [L,R] (1-indexed)
        pair<long long,long long> lteCountSum(int L, int R, int x) const {
            if (L > R || x < lo) return {0LL, 0LL};
            if (hi <= x) {
                long long cnt = R - L + 1LL;
                long long sum = prefAll[R] - prefAll[L - 1];
                return {cnt, sum};
            }
            if (lo == hi) {
                // here lo==hi>x cannot happen due to previous checks
                long long cnt = R - L + 1LL;
                long long sum = prefAll[R] - prefAll[L - 1];
                return {cnt, sum};
            }
            int mid = lo + (hi - lo) / 2;
            int leftCount = b[R] - b[L - 1];
            long long leftSum = sLeft[R] - sLeft[L - 1];
            if (x <= mid) {
                if (!l) return {0LL, 0LL};
                int nL = b[L - 1] + 1;
                int nR = b[R];
                return l->lteCountSum(nL, nR, x);
            } else {
                pair<long long,long long> resL = {leftCount, leftSum};
                if (!r) return resL;
                int nL = L - b[L - 1];
                int nR = R - b[R];
                auto resR = r->lteCountSum(nL, nR, x);
                return {resL.first + resR.first, resL.second + resR.second};
            }
        }
    };

    struct SparseMinMax {
        int n = 0;
        int LG = 0;
        vector<int> lg;
        vector<vector<int>> stMin, stMax;

        SparseMinMax() {}
        SparseMinMax(const vector<int>& a) { build(a); }

        void build(const vector<int>& a) {
            n = (int)a.size();
            LG = 1;
            while ((1 << LG) <= n) LG++;
            stMin.assign(LG, vector<int>(n));
            stMax.assign(LG, vector<int>(n));
            stMin[0] = a;
            stMax[0] = a;
            for (int j = 1; j < LG; j++) {
                int len = 1 << j;
                int half = len >> 1;
                for (int i = 0; i + len <= n; i++) {
                    stMin[j][i] = min(stMin[j-1][i], stMin[j-1][i+half]);
                    stMax[j][i] = max(stMax[j-1][i], stMax[j-1][i+half]);
                }
            }
            lg.assign(n + 1, 0);
            for (int i = 2; i <= n; i++) lg[i] = lg[i/2] + 1;
        }

        pair<int,int> query(int l, int r) const {
            int len = r - l + 1;
            int p = lg[len];
            int span = 1 << p;
            int mn = min(stMin[p][l], stMin[p][r - span + 1]);
            int mx = max(stMax[p][l], stMax[p][r - span + 1]);
            return {mn, mx};
        }
    };

public:
    vector<long long> minOperations(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = (int)nums.size();
        vector<int> rem(n), b(n);
        for (int i = 0; i < n; i++) {
            rem[i] = nums[i] % k;
            b[i] = nums[i] / k;
        }

        SparseMinMax rmq(rem);

        int mnB = *min_element(b.begin(), b.end());
        int mxB = *max_element(b.begin(), b.end());
        WaveletTree wt(b, mnB, mxB);

        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + (long long)b[i];

        vector<long long> ans;
        ans.reserve(queries.size());

        for (auto &q : queries) {
            int l = q[0], r = q[1];
            auto [mnR, mxR] = rmq.query(l, r);
            if (mnR != mxR) {
                ans.push_back(-1);
                continue;
            }
            int len = r - l + 1;
            if (len == 1) {
                ans.push_back(0);
                continue;
            }
            int L = l + 1, R = r + 1; // wavelet tree uses 1-indexed positions
            int med = wt.kth(L, R, (len + 1) / 2);
            auto [cntL, sumL] = wt.lteCountSum(L, R, med);
            long long total = pref[r + 1] - pref[l];
            long long sumR = total - sumL;
            long long cntR = len - cntL;
            long long ops = 1LL * med * cntL - sumL + (sumR - 1LL * med * cntR);
            ans.push_back(ops);
        }
        return ans;
    }
};
// @lc code=end
