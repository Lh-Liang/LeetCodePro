#
# @lc app=leetcode id=3420 lang=cpp
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#
# @lc code=start
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        long long count = 0;
        int n = nums.size(), left = 0;
        vector<int> operations(n, 0);
        for (int right = 1; right < n; ++right) {
            if (nums[right] < nums[right - 1]) {
                operations[right] = nums[right - 1] - nums[right];
            }
            operations[right] += operations[right - 1];
            while (operations[right] - (left > 0 ? operations[left - 1] : 0) > k) {
                ++left;
            }
            count += right - left + 1;
        }
        return count + n; // Include single element subarrays which are always non-decreasing.
    }
};
# @lc code=end