# \@lc app=leetcode id=3510 lang=java
#
# [3510] Minimum Pair Removal to Sort Array II
#
\@lc code=start
class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;
        
        // dp[i] represents the minimum operations needed to make nums[0..i] non-decreasing
        int[] dp = new int[n];
        
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i - 1]; // Initially, assume no operation is needed beyond previous
            if (nums[i] < nums[i - 1]) {
                // Calculate sum and decide if replacement helps based on future states
                int sum = nums[i] + nums[i - 1];
                // Check against future elements with sum as new position value
                if (i + 1 < n && sum > nums[i + 1]) {
                    dp[i] = Math.min(dp[i], dp[i - 1] + 1); // Consider replacement if beneficial
                } else {
                    dp[i] = dp[i - 1] + 1; // Replace current pair since it's decreasing
                }
            }
        }
        
        return dp[n - 1];
    }
}
# \@lc code=end