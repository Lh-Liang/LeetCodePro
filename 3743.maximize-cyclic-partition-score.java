# @lc app=leetcode id=3743 lang=java
# [3743] Maximize Cyclic Partition Score
#
# @lc code=start
class Solution {
    public long maximumScore(int[] nums, int k) {
        int n = nums.length;
        long maxScore = 0;
        long[][] dp = new long[n][k + 1];
        
        // Iterate over all possible starting points to simulate cyclic nature
        for (int start = 0; start < n; start++) {
            // Reset DP for each new starting point cycle simulation
            for (long[] row : dp) Arrays.fill(row, Long.MIN_VALUE);
            
            // Initialize base case for single partition subarrays
            long minVal = nums[start], maxVal = nums[start];
            for (int len = 1; len <= n; len++) {
                int currentIndex = (start + len - 1) % n;
                minVal = Math.min(minVal, nums[currentIndex]);
                maxVal = Math.max(maxVal, nums[currentIndex]);
                long rangeScore = maxVal - minVal;
                
                // Update DP table where partition count is at least one
                dp[start][1] = Math.max(dp[start][1], rangeScore);
                
                // Update DP table for possible further partitions >1
                for (int m = 2; m <= k; m++) {
                    if (len < n) { // Ensure we don't complete a full loopback in one go except final partition
                        int nextStartIdx = (currentIndex + 1) % n;
                        if (dp[nextStartIdx][m - 1] != Long.MIN_VALUE) {
                            dp[start][m] = Math.max(dp[start][m], rangeScore + dp[nextStartIdx][m - 1]);
                        }
                    }
                }
            }
            maxScore = Math.max(maxScore, dp[start][k]);
        }
        return maxScore;
    }
}
# @lc code=end