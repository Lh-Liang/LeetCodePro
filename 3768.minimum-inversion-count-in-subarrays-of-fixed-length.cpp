# @lc app=leetcode id=3768 lang=cpp
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#
# @lc code=start
class Solution {
public:
    long long minInversionCount(vector<int>& nums, int k) {
        int n = nums.size();
        long long min_inv_count = LLONG_MAX;
        vector<int> bit(n + 1, 0);
        auto update = [&](int idx, int val) {
            while (idx <= n) {
                bit[idx] += val;
                idx += idx & -idx;
            }
        };
        auto query = [&](int idx) {
            int sum = 0;
            while (idx > 0) {
                sum += bit[idx];
                idx -= idx & -idx;
            }
            return sum;
        };
        for (int i = 0; i < k; ++i) {
            update(nums[i], 1);
        }
        long long current_inv_count = 0;
        for (int i = 0; i < k; ++i) {
            current_inv_count += query(n) - query(nums[i]);
        }
        min_inv_count = min(min_inv_count, current_inv_count);
        for (int i = k; i < n; ++i) {
            update(nums[i - k], -1); // Remove element going out of window. " update(nums[i], 1); // Add new element into window. " // Calculate inversions with new element added into the window. " current_inv_count -= query(nums[i - k] - 1); " current_inv_count += query(n) - query(nums[i]); " min_inv_count = min(min_inv_count, current_inv_count); " } " return min_inv_count; " } " }; " # @lc code=end