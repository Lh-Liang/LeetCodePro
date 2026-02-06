#
# @lc app=leetcode id=3413 lang=java
#
# [3413] Maximum Coins From K Consecutive Bags
#
# @lc code=start
class Solution {
    public long maximumCoins(int[][] coins, int k) {
        Arrays.sort(coins, (a, b) -> Integer.compare(a[0], b[0]));
        int n = coins.length;
        int left = 0, right = 0;
        long sum = 0, max = 0;
        long windowStart = coins[0][0];
        long windowEnd = windowStart + k - 1;

        // precompute the total number of bags
        while (right < n && coins[right][1] < windowStart) right++;

        long l = windowStart;
        while (true) {
            // Reset sum for each window
            sum = 0;
            long curL = l, curR = l + k - 1;
            int idx = 0;
            while (idx < n && coins[idx][1] < curL) idx++;
            int j = idx;
            while (j < n && coins[j][0] <= curR) {
                long segL = Math.max(coins[j][0], curL);
                long segR = Math.min(coins[j][1], curR);
                if (segL <= segR) {
                    sum += (segR - segL + 1) * coins[j][2];
                }
                j++;
            }
            max = Math.max(max, sum);
            // Move window forward
            // Find next possible l: the next start of any interval or current l + 1, whichever is minimal, but not beyond possible window range
            long nextL = l + 1;
            if (idx < n) {
                nextL = Math.max(nextL, Math.min(coins[idx][1] + 1, l + 1));
            }
            // Stop if window exceeds range
            if (j >= n && (idx >= n || coins[n - 1][1] < nextL)) break;
            l = nextL;
        }
        return max;
    }
}
# @lc code=end