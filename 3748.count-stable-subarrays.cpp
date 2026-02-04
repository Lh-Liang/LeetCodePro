#
# @lc app=leetcode id=3748 lang=cpp
#
# [3748] Count Stable Subarrays
#
# @lc code=start
class Solution {
public:
    vector<long long> countStableSubarrays(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> seg_start(n), seg_end(n);
        int l = 0;
        while (l < n) {
            int r = l;
            while (r + 1 < n && nums[r] <= nums[r + 1]) ++r;
            for (int k = l; k <= r; ++k) {
                seg_start[k] = l;
                seg_end[k] = r;
            }
            l = r + 1;
        }
        vector<long long> result;
        for (auto& q : queries) {
            int left = q[0], right = q[1];
            long long ans = 0;
            int i = left;
            while (i <= right) {
                int s = max(i, seg_start[i]);
                int e = min(seg_end[i], right);
                long long len = e - s + 1;
                ans += len * (len + 1) / 2;
                i = e + 1;
            }
            result.push_back(ans);
        }
        return result;
    }
};
# @lc code=end