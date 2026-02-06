#
# @lc app=leetcode id=3420 lang=java
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#
# @lc code=start
class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.length;
        long result = 0;
        for (int i = 0; i < n; ++i) {
            long ops = 0;
            int prev = nums[i];
            result++; // single element subarray is always valid
            for (int j = i + 1; j < n; ++j) {
                if (nums[j] < prev) {
                    ops += (prev - nums[j]);
                }
                if (ops > k) break;
                prev = Math.max(prev, nums[j]);
                result++;
            }
        }
        return result;
    }
}
# @lc code=end