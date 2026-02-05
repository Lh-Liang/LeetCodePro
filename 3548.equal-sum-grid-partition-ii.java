#
# @lc app=leetcode id=3548 lang=java
#
# [3548] Equal Sum Grid Partition II
#
# @lc code=start
class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int total = 0;
        int[] rowSum = new int[m];
        int[] colSum = new int[n];
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) {
                total += grid[i][j];
                rowSum[i] += grid[i][j];
                colSum[j] += grid[i][j];
            }
        // Horizontal cuts
        int topSum = 0;
        for (int cut = 0; cut < m - 1; ++cut) {
            topSum += rowSum[cut];
            int botSum = total - topSum;
            if (topSum == botSum) return true;
            int diff = Math.abs(topSum - botSum);
            if (diff > 0) {
                for (int j = 0; j < n; ++j) {
                    // Discount from top section
                    if (topSum > botSum && grid[cut][j] == diff && m > 1 && n > 1) {
                        if (sectionCheck(grid, 0, cut, 0, n-1, cut, j, diff)) return true;
                    }
                    // Discount from bottom section
                    if (botSum > topSum && grid[cut+1][j] == diff && m > 1 && n > 1) {
                        if (sectionCheck(grid, cut+1, m-1, 0, n-1, cut+1, j, diff)) return true;
                    }
                }
            }
        }
        // Vertical cuts
        int leftSum = 0;
        for (int cut = 0; cut < n - 1; ++cut) {
            leftSum += colSum[cut];
            int rightSum = total - leftSum;
            if (leftSum == rightSum) return true;
            int diff = Math.abs(leftSum - rightSum);
            if (diff > 0) {
                for (int i = 0; i < m; ++i) {
                    // Discount from left section
                    if (leftSum > rightSum && grid[i][cut] == diff && m > 1 && n > 1) {
                        if (sectionCheck(grid, 0, m-1, 0, cut, i, cut, diff)) return true;
                    }
                    // Discount from right section
                    if (rightSum > leftSum && grid[i][cut+1] == diff && m > 1 && n > 1) {
                        if (sectionCheck(grid, 0, m-1, cut+1, n-1, i, cut+1, diff)) return true;
                    }
                }
            }
        }
        return false;
    }
    // Systematic connectivity check for remaining section after removing (remR, remC)
    private boolean sectionCheck(int[][] grid, int r1, int r2, int c1, int c2, int remR, int remC, int diff) {
        int m = r2 - r1 + 1;
        int n = c2 - c1 + 1;
        if (m * n <= 1) return false; // would make section empty
        // Mark the section and remove the cell
        boolean[][] mask = new boolean[m][n];
        int cells = 0;
        for (int i = r1; i <= r2; ++i) {
            for (int j = c1; j <= c2; ++j) {
                if (i == remR && j == remC) continue;
                mask[i - r1][j - c1] = true;
                cells++;
            }
        }
        // Find a connected component (BFS/DFS)
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        boolean found = false;
        int startX = -1, startY = -1;
        outer:
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mask[i][j]) { startX = i; startY = j; found = true; break outer; }
            }
        }
        if (!found) return false;
        boolean[][] vis = new boolean[m][n];
        java.util.Queue<int[]> queue = new java.util.LinkedList<>();
        queue.add(new int[]{startX, startY});
        vis[startX][startY] = true;
        int seen = 1;
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            for (int d = 0; d < 4; ++d) {
                int ni = p[0] + dx[d], nj = p[1] + dy[d];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && mask[ni][nj] && !vis[ni][nj]) {
                    vis[ni][nj] = true;
                    queue.add(new int[]{ni, nj});
                    seen++;
                }
            }
        }
        return seen == cells;
    }
}
# @lc code=end