class Solution {
    public long maximumScore(int[] nums, int k) {
        int n = nums.length;
        int[] arr = new int[2 * n];
        for (int i = 0; i < 2 * n; ++i) arr[i] = nums[i % n];
        long[][] minVal = new long[2 * n][n + 1];
        long[][] maxVal = new long[2 * n][n + 1];
        for (int i = 0; i < 2 * n; ++i) {
            long mi = arr[i], ma = arr[i];
            minVal[i][1] = mi; maxVal[i][1] = ma;
            for (int len = 2; len <= n && i + len - 1 < 2 * n; ++len) {
                mi = Math.min(mi, arr[i + len - 1]);
                ma = Math.max(ma, arr[i + len - 1]);
                minVal[i][len] = mi; maxVal[i][len] = ma;
            }
        }
        long ans = 0;
        for (int start = 0; start < n; ++start) {
            long[][] dp = new long[n + 1][k + 1];
            for (int len = 1; len <= n; ++len) {
                for (int t = 1; t <= Math.min(k, len); ++t) {
                    if (t == 1) {
                        dp[len][t] = maxVal[start][len] - minVal[start][len];
                    } else {
                        for (int cut = 1; cut < len; ++cut) {
                            if (t - 1 <= cut) {
                                dp[len][t] = Math.max(dp[len][t], dp[cut][t - 1] + maxVal[start + cut][len - cut] - minVal[start + cut][len - cut]);
                            }
                        }
                    }
                }
            }
            for (int t = 1; t <= k; ++t) ans = Math.max(ans, dp[n][t]);
        }
        return ans;
    }
}