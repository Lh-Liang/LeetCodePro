#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#
#include <bits/stdc++.h>
using namespace std;

# @lc code=start
class Solution {
    struct Node {
        int sum;      // total sum in segment
        int minPref;  // min prefix sum over non-empty prefixes
        int maxPref;  // max prefix sum over non-empty prefixes
    };

    struct SegTree {
        int n;
        vector<Node> st;

        SegTree(int n_) : n(n_), st(4 * n_ + 4) {
            build(1, 1, n);
        }

        static Node mergeNode(const Node &L, const Node &R) {
            Node res;
            res.sum = L.sum + R.sum;
            // prefixes either fully in L, or span L and into R
            res.minPref = min(L.minPref, L.sum + R.minPref);
            res.maxPref = max(L.maxPref, L.sum + R.maxPref);
            return res;
        }

        void build(int p, int l, int r) {
            if (l == r) {
                st[p] = {0, 0, 0};
                return;
            }
            int m = (l + r) >> 1;
            build(p << 1, l, m);
            build(p << 1 | 1, m + 1, r);
            st[p] = mergeNode(st[p << 1], st[p << 1 | 1]);
        }

        void update(int idx, int val) { update(1, 1, n, idx, val); }

        void update(int p, int l, int r, int idx, int val) {
            if (l == r) {
                st[p] = {val, val, val};
                return;
            }
            int m = (l + r) >> 1;
            if (idx <= m) update(p << 1, l, m, idx, val);
            else update(p << 1 | 1, m + 1, r, idx, val);
            st[p] = mergeNode(st[p << 1], st[p << 1 | 1]);
        }

        // Find the smallest index pos in [1..limit] such that prefixSum(pos) == target.
        // Returns INF if not found.
        int findFirst(int limit, int target) {
            if (limit <= 0) return (int)1e9;
            return findFirst(1, 1, n, 0LL, limit, target);
        }

        int findFirst(int p, int l, int r, long long pre, int limit, int target) {
            if (l > limit) return (int)1e9;

            if (r <= limit) {
                long long lo = pre + st[p].minPref;
                long long hi = pre + st[p].maxPref;
                if (target < lo || target > hi) return (int)1e9;
                if (l == r) {
                    // only non-empty prefix is the leaf itself
                    return l;
                }
                int m = (l + r) >> 1;
                int lc = p << 1, rc = p << 1 | 1;
                long long llo = pre + st[lc].minPref;
                long long lhi = pre + st[lc].maxPref;
                if (target >= llo && target <= lhi) {
                    return findFirst(lc, l, m, pre, limit, target);
                }
                return findFirst(rc, m + 1, r, pre + st[lc].sum, limit, target);
            }

            int m = (l + r) >> 1;
            int lc = p << 1, rc = p << 1 | 1;
            int leftRes = findFirst(lc, l, m, pre, limit, target);
            if (leftRes != (int)1e9) return leftRes;
            return findFirst(rc, m + 1, r, pre + st[lc].sum, limit, target);
        }
    };

public:
    int longestBalanced(vector<int>& nums) {
        int n = (int)nums.size();
        SegTree seg(n);

        const int MAXV = 100000;
        vector<int> last(MAXV + 1, 0);

        int diff = 0; // totalDistinctEven - totalDistinctOdd among values seen so far
        int ans = 0;

        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            int sign = (x % 2 == 0) ? 1 : -1;

            if (last[x] != 0) {
                seg.update(last[x], 0); // remove old last occurrence marker
            } else {
                diff += sign; // new distinct value affects totals
            }

            seg.update(i, sign); // add new last occurrence marker
            last[x] = i;

            int target = diff;
            int limit = i - 1;

            int k = -1; // k = l-1
            if (target == 0) {
                k = 0; // prefixSum(0) == 0
            } else {
                int idx = seg.findFirst(limit, target);
                if (idx != (int)1e9) k = idx;
            }

            if (k != -1) {
                ans = max(ans, i - k);
            }
        }

        return ans;
    }
};
# @lc code=end
