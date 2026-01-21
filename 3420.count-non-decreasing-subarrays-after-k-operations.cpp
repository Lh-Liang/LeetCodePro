#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3420 lang=cpp
 *
 * [3420] Count Non-Decreasing Subarrays After K Operations
 */

// @lc code=start
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = (int)nums.size();
        int n1 = n + 1;

        // prefix sums
        vector<long long> pref(n1, 0);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];

        // nxt[i] = next index > i with nums[nxt] > nums[i], else n
        vector<int> nxt(n1, n);
        vector<int> st;
        st.reserve(n);
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && nums[st.back()] <= nums[i]) st.pop_back();
            nxt[i] = st.empty() ? n : st.back();
            st.push_back(i);
        }
        nxt[n] = n;

        // segCost for full segment [i, nxt[i)-1]
        vector<long long> segCost(n1, 0);
        for (int i = 0; i < n; i++) {
            int j = nxt[i];
            long long len = (long long)(j - i);
            long long maxSum = 1LL * nums[i] * len;
            long long sumSeg = pref[j] - pref[i];
            segCost[i] = maxSum - sumSeg;
        }
        segCost[n] = 0;

        // binary lifting tables
        int LOG = 0;
        while ((1 << LOG) <= n1) LOG++;

        vector<int> up(LOG * n1, n);
        vector<long long> sc(LOG * n1, 0);
        auto ID = [n1](int j, int i) { return j * n1 + i; };

        for (int i = 0; i <= n; i++) {
            up[ID(0, i)] = nxt[i];
            sc[ID(0, i)] = segCost[i];
        }
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i <= n; i++) {
                int mid = up[ID(j - 1, i)];
                up[ID(j, i)] = up[ID(j - 1, mid)];
                sc[ID(j, i)] = sc[ID(j - 1, i)] + sc[ID(j - 1, mid)];
            }
        }

        auto costQuery = [&](int l, int r) -> long long {
            int cur = l;
            long long res = 0;

            for (int j = LOG - 1; j >= 0; j--) {
                int to = up[ID(j, cur)];
                if (to <= r + 1) { // full segments up to to-1 are within [l..r]
                    res += sc[ID(j, cur)];
                    cur = to;
                    if (cur == n) break;
                }
            }

            // partial last segment [cur..r]
            long long len = (long long)(r - cur + 1);
            long long maxSum = 1LL * nums[cur] * len;
            long long sumSeg = pref[r + 1] - pref[cur];
            res += (maxSum - sumSeg);
            return res;
        };

        long long ans = 0;
        int l = 0;
        for (int r = 0; r < n; r++) {
            while (l <= r && costQuery(l, r) > (long long)k) l++;
            ans += (r - l + 1);
        }
        return ans;
    }
};
// @lc code=end
