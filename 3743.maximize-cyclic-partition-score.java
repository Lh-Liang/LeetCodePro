#
# @lc app=leetcode id=3743 lang=java
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution {
    public long maximumScore(int[] nums, int k) {
        int n = nums.length;
        long maxScore = 0;
        int[] arr = new int[2 * n];
        for (int i = 0; i < 2 * n; ++i) arr[i] = nums[i % n];
        // Precompute min and max for all subarrays of length <= n
        long[][] minTable = new long[2 * n][n + 1];
        long[][] maxTable = new long[2 * n][n + 1];
        for (int i = 0; i < 2 * n; ++i) {
            minTable[i][0] = Integer.MAX_VALUE;
            maxTable[i][0] = Integer.MIN_VALUE;
            for (int len = 1; len <= n && i + len <= 2 * n; ++len) {
                if (len == 1) {
                    minTable[i][len] = arr[i];
                    maxTable[i][len] = arr[i];
                } else {
                    minTable[i][len] = Math.min(minTable[i][len - 1], arr[i + len - 1]);
                    maxTable[i][len] = Math.max(maxTable[i][len - 1], arr[i + len - 1]);
                }
            }
        }
        // Try all starting points
        for (int start = 0; start < n; ++start) {
            // DP: dp[i][j] = max score for prefix length i (from start), with j partitions
            long[][] dp = new long[n + 1][k + 1];
            for (int i = 0; i <= n; ++i) for (int j = 0; j <= k; ++j) dp[i][j] = Long.MIN_VALUE;
            dp[0][0] = 0;
            for (int i = 1; i <= n; ++i) {
                for (int part = 1; part <= Math.min(i, k); ++part) {
                    for (int last = part - 1; last < i; ++last) {
                        long range = maxTable[start + last][i - last] - minTable[start + last][i - last];
                        if (dp[last][part - 1] != Long.MIN_VALUE) {
                            dp[i][part] = Math.max(dp[i][part], dp[last][part - 1] + range);
                        }
                    }
                }
            }
            // Get the max for this rotation
            for (int part = 1; part <= k; ++part) {
                maxScore = Math.max(maxScore, dp[n][part]);
            }
        }
        return maxScore;
    }
}
# @lc code=end