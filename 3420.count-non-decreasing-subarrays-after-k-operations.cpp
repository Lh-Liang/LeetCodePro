#
# @lc app=leetcode id=3420 lang=cpp
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        // Implementing a sliding window approach with optimizations.
        long long count = 0;
        int n = nums.size();
        for (int start = 0; start < n; ++start) {
            int ops_needed = 0;
            for (int end = start; end < n; ++end) {
                if (end > start && nums[end] < nums[end - 1]) {
                    ops_needed += nums[end - 1] - nums[end];
                }
                if (ops_needed <= k) {
                    ++count; // Valid subarray found.
                } else {
                    break; // No point in continuing as ops_needed exceeded k.
                }
            }
        }
        return count;
    }
};
# @lc code=end