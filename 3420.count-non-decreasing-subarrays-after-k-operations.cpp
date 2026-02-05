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
        long long ans = 0;
        for (int left = 0; left < n; ++left) {
            long long used = 0;
            int max_val = nums[left];
            for (int right = left + 1; right < n; ++right) {
                if (nums[right] < max_val) {
                    used += max_val - nums[right];
                    if (used > k) break;
                } else {
                    max_val = nums[right];
                }
            }
            // The number of valid subarrays starting at left is (right - left)
            ans += (right - left);
        }
        return ans;
    }
};
# @lc code=end