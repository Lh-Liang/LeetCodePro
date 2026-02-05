#
# @lc app=leetcode id=3640 lang=java
#
# [3640] Trionic Array II
#

# @lc code=start
class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        if (n < 4) return Long.MIN_VALUE; // Handle edge case where no trionic can exist
        
        long[] incLeft = new long[n];
        long[] incRight = new long[n];
        long[] decMiddle = new long[n];

        // Fill incLeft array: Maximum sum of strictly increasing subarray ending at each position
        incLeft[0] = nums[0];
        for (int i = 1; i < n; i++) {
            incLeft[i] = (nums[i] > nums[i-1]) ? incLeft[i-1] + nums[i] : nums[i];
        }

        // Fill incRight array: Maximum sum of strictly increasing subarray starting at each position
        incRight[n-1] = nums[n-1];
        for (int i = n-2; i >= 0; i--) {
            incRight[i] = (nums[i] < nums[i+1]) ? incRight[i+1] + nums[i] : nums[i];
        }

        // Fill decMiddle array: Maximum sum of strictly decreasing subarray ending at each position
        decMiddle[1] = Long.MIN_VALUE;
        for (int i = 2; i < n-1; i++) {
            if (nums[i-1] > nums[i]) {
                decMiddle[i] = (decMiddle[i-1] != Long.MIN_VALUE ? decMiddle[i-1] : 0) + nums[i];
            } else {
                decMiddle[i] = Long.MIN_VALUE;
            }
        }

        // Calculate maximum trionic subarray sum using dynamic programming arrays
        long maxSum = Long.MIN_VALUE;
        for (int p = 1; p < n-2; p++) { // p starts from 1, q ends before n-2
            if (nums[p-1] >= nums[p]) continue; // Ensure l...p is valid increasing before checking mid
            
            for (int q = p+1; q < n-1; q++) {
                if (decMiddle[q] != Long.MIN_VALUE && nums[q+1] > nums[q]) { 
                    maxSum = Math.max(maxSum, incLeft[p-1] + decMiddle[q] + incRight[q+1]);
                }
            }
        }

        return maxSum;
    }
}
# @lc code=end