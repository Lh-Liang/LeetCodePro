#
# @lc app=leetcode id=3640 lang=java
#
# [3640] Trionic Array II
#
# @lc code=start
class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        // Precompute strictly increasing to the left (ending at i)
        long[] incLeftSum = new long[n];
        int[] incLeftLen = new int[n];
        incLeftSum[0] = nums[0]; incLeftLen[0] = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i - 1] < nums[i]) {
                incLeftSum[i] = incLeftSum[i - 1] + nums[i];
                incLeftLen[i] = incLeftLen[i - 1] + 1;
            } else {
                incLeftSum[i] = nums[i];
                incLeftLen[i] = 1;
            }
        }
        // Precompute strictly increasing to the right (starting at i)
        long[] incRightSum = new long[n];
        int[] incRightLen = new int[n];
        incRightSum[n - 1] = nums[n - 1]; incRightLen[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                incRightSum[i] = incRightSum[i + 1] + nums[i];
                incRightLen[i] = incRightLen[i + 1] + 1;
            } else {
                incRightSum[i] = nums[i];
                incRightLen[i] = 1;
            }
        }
        // Precompute strictly decreasing to the left (ending at i)
        long[] decLeftSum = new long[n];
        int[] decLeftLen = new int[n];
        decLeftSum[0] = nums[0]; decLeftLen[0] = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i - 1] > nums[i]) {
                decLeftSum[i] = decLeftSum[i - 1] + nums[i];
                decLeftLen[i] = decLeftLen[i - 1] + 1;
            } else {
                decLeftSum[i] = nums[i];
                decLeftLen[i] = 1;
            }
        }
        // Precompute strictly decreasing to the right (starting at i)
        long[] decRightSum = new long[n];
        int[] decRightLen = new int[n];
        decRightSum[n - 1] = nums[n - 1]; decRightLen[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] > nums[i + 1]) {
                decRightSum[i] = decRightSum[i + 1] + nums[i];
                decRightLen[i] = decRightLen[i + 1] + 1;
            } else {
                decRightSum[i] = nums[i];
                decRightLen[i] = 1;
            }
        }
        long maxSum = Long.MIN_VALUE;
        // For each possible q (center of decreasing segment), try to expand to left and right
        for (int q = 1; q < n - 1; q++) {
            int decLen = decLeftLen[q];
            if (decLen < 2) continue; // strictly decreasing needs at least 2
            int p = q - decLen + 1; // p...q is decreasing
            // Left: find maximal strictly increasing ending at p-1
            if (p - 1 < 1) continue; // need at least two elements left for increasing
            int incLeftEnd = p - 1;
            int incLen = incLeftLen[incLeftEnd];
            if (incLen < 2) continue; // strictly increasing needs at least 2
            int l = incLeftEnd - incLen + 1;
            // Right: find maximal strictly increasing starting at q+1
            if (q + 1 >= n - 1) continue; // need at least two right
            int incRightStart = q + 1;
            int incRightLenVal = incRightLen[incRightStart];
            if (incRightLenVal < 2) continue;
            int r = incRightStart + incRightLenVal - 1;
            if (l >= p || p >= q || q >= r) continue;
            // Compute sum
            long sum = 0;
            // increasing left: l...p-1
            sum += incLeftSum[incLeftEnd];
            if (l > 0) sum -= incLeftSum[l - 1];
            // decreasing: p...q
            sum += decLeftSum[q];
            if (p > 0) sum -= decLeftSum[p - 1];
            // increasing right: q+1...r
            sum += incRightSum[incRightStart];
            if (r + 1 < n) sum -= incRightSum[r + 1];
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum;
    }
}
# @lc code=end