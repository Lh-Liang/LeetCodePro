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
        vector<long long> prefix(n, 0);
        // prefix[i]: sum of max(0, nums[j-1] - nums[j]) for j in 1..i
        for(int i = 1; i < n; ++i) {
            prefix[i] = prefix[i-1] + max(0, nums[i-1] - nums[i]);
        }
        long long ans = 0;
        int r = 0;
        for(int l = 0; l < n; ++l) {
            // For current l, move r as far as possible: prefix[r]-prefix[l] <= k
            if (r < l) r = l;
            while(r < n && prefix[r] - prefix[l] <= k) {
                ++r;
            }
            ans += r - l;
        }
        return ans;
    }
};
# @lc code=end