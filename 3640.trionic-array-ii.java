#
# @lc app=leetcode id=3640 lang=java
#
# [3640] Trionic Array II
#
# @lc code=start
class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        long[] leftMax = new long[n];
        long[] rightMax = new long[n];
        long sum = 0;
        // Calculate left max sums
        for (int i = 1; i < n - 2; i++) {
            sum += nums[i];
            if (nums[i] > nums[i - 1]) {
                leftMax[i] = Math.max(leftMax[i - 1] + nums[i], nums[i]);
            } else {
                leftMax[i] = leftMax[i - 1];
            }
        }
        // Calculate right max sums
        sum = 0;
        for (int i = n - 2; i >= 2; i--) {
            sum += nums[i];
            if (nums[i] < nums[i + 1]) {
                rightMax[i] = Math.max(rightMax[i + 1] + nums[i], nums[i]);
            } else {
                rightMax[i] = rightMax[i + 1];
            }
        }
        // Calculate maximum trionic sum using middle element as pivot point p,q in increasing-decreasing-increasing pattern. "num[l..p..q..r]" & calculate max sum. "left-max[p]", current middle sum "nums[p]+nums[q]", "right-max[q]". & Calculate max of these combined sums as final result. & Return that max result. & Finalize test case results