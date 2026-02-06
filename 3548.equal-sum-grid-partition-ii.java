#
# @lc app=leetcode id=3548 lang=java
#
# [3548] Equal Sum Grid Partition II
#
# @lc code=start
class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        long[][] prefix = new long[m+1][n+1];
        // Compute prefix sum
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                prefix[i+1][j+1] = grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j];
            }
        }
        long total = prefix[m][n];
        // Try all horizontal cuts
        for (int cut = 1; cut < m; ++cut) {
            long top = prefix[cut][n];
            long bot = total - top;
            if (top == bot) return true;
            // Try removing a border cell from top section
            for (int j = 0; j < n; ++j) {
                if (top - grid[cut-1][j] == bot) return true;
            }
            // Try removing a border cell from bottom section
            for (int j = 0; j < n; ++j) {
                if (bot - grid[cut][j] == top) return true;
            }
        }
        // Try all vertical cuts
        for (int cut = 1; cut < n; ++cut) {
            long left = 0L;
            for (int i = 0; i < m; ++i) left += prefix[i+1][cut] - prefix[i][cut];
            long leftSum = 0L, rightSum = 0L;
            leftSum = 0L;
            for (int i = 0; i < m; ++i) leftSum += prefix[i+1][cut] - prefix[i][cut];
            leftSum = prefix[m][cut];
            rightSum = total - leftSum;
            if (leftSum == rightSum) return true;
            // Try removing a border cell from left section
            for (int i = 0; i < m; ++i) {
                if (leftSum - grid[i][cut-1] == rightSum) return true;
            }
            // Try removing a border cell from right section
            for (int i = 0; i < m; ++i) {
                if (rightSum - grid[i][cut] == leftSum) return true;
            }
        }
        return false;
    }
}
# @lc code=end