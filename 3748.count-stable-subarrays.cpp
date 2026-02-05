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
        vector<int> run_start(n), run_end(n);
        // Precompute the runs
        int l = 0;
        while (l < n) {
            int r = l;
            while (r + 1 < n && nums[r] <= nums[r+1]) ++r;
            for (int i = l; i <= r; ++i) {
                run_start[i] = l;
                run_end[i] = r;
            }
            l = r + 1;
        }
        // Precompute prefix sums of stable subarrays count up to each position
        vector<long long> prefix(n+1);
        int i = 0;
        while (i < n) {
            int j = run_end[i];
            long long len = j - i + 1;
            long long cnt = len * (len + 1) / 2;
            prefix[j+1] = prefix[i] + cnt;
            i = j + 1;
        }
        // Compute answer for each query
        vector<long long> ans;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            long long res = 0;
            int i = l;
            while (i <= r) {
                int seg_r = min(run_end[i], r);
                long long len = seg_r - i + 1;
                res += len * (len + 1) / 2;
                i = seg_r + 1;
            }
            ans.push_back(res);
        }
        return ans;
    }
};
# @lc code=end