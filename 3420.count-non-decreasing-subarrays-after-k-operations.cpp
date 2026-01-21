#
# @lc app=leetcode id=3420 lang=cpp
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            pref[i] = pref[i - 1] + nums[i - 1];
        }
        long long kk = k;
        long long ans = 0;
        int cur_r = n - 1;
        long long cur_pmaxv = nums[n - 1];
        ans += 1;
        for (int st = n - 2; st >= 0; --st) {
            long long v = nums[st];
            bool dom = (v >= cur_pmaxv);
            int maxr = cur_r;
            if (dom) {
                int lo = st;
                int hi = maxr;
                while (lo <= hi) {
                    int mid = lo + (hi - lo) / 2;
                    long long lenb = (long long)mid - st + 1;
                    long long sumb = pref[mid + 1] - pref[st];
                    long long costb = lenb * v - sumb;
                    if (costb <= kk) {
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }
                cur_r = hi;
                cur_pmaxv = v;
            }
            // else keep as is
            ans += (long long)cur_r - st + 1;
        }
        return ans;
    }
};
# @lc code=end