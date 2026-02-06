#
# @lc app=leetcode id=3459 lang=java
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#

# @lc code=start
class Solution {
    public int lenOfVDiagonal(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        // Directions: [down-right, up-left, down-left, up-right]
        int[][] dirs = { {1,1}, {-1,-1}, {1,-1}, {-1,1} };
        // Clockwise turn: 0->2, 2->1, 1->3, 3->0
        int[] turn = {2,3,1,0};
        int[][][] dp = new int[n][m][4];
        // Precompute DP for each direction
        for (int d = 0; d < 4; ++d) {
            int dx = dirs[d][0], dy = dirs[d][1];
            int sx = dx > 0 ? 0 : n - 1;
            int sy = dy > 0 ? 0 : m - 1;
            int ex = dx > 0 ? n : -1;
            int ey = dy > 0 ? m : -1;
            for (int i = sx; i != ex; i += dx > 0 ? 1 : -1) {
                for (int j = sy; j != ey; j += dy > 0 ? 1 : -1) {
                    if (grid[i][j] == 1) {
                        dp[i][j][d] = 1;
                    } else if ((dx > 0 ? i - dx >= 0 : i - dx < n) && (dy > 0 ? j - dy >= 0 : j - dy < m)) {
                        int prevX = i - dx, prevY = j - dy;
                        int prev = dp[prevX][prevY][d];
                        int expected = (prev % 2 == 1) ? 2 : 0;
                        if (grid[i][j] == expected) {
                            dp[i][j][d] = prev + 1;
                        }
                    }
                }
            }
        }
        int maxLen = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] != 1) continue;
                for (int d = 0; d < 4; ++d) {
                    int len1 = dp[i][j][d];
                    int x = i, y = j;
                    int dx = dirs[d][0], dy = dirs[d][1];
                    // Move as far as possible in this direction
                    for (int k = 1; k < len1; ++k) {
                        x += dx;
                        y += dy;
                    }
                    // Try to turn at this point (if inside grid)
                    if (x >= 0 && x < n && y >= 0 && y < m) {
                        int td = turn[d];
                        int len2 = 0;
                        int tx = x, ty = y;
                        int tdx = dirs[td][0], tdy = dirs[td][1];
                        // Avoid overlapping the turn cell
                        while (true) {
                            tx += tdx;
                            ty += tdy;
                            if (tx < 0 || tx >= n || ty < 0 || ty >= m) break;
                            int step = tx - x + ty - y;
                            // The sequence should continue alternating
                            int expected = ((len1 + step) % 2 == 1) ? 2 : 0;
                            if (grid[tx][ty] != expected) break;
                            len2++;
                        }
                        maxLen = Math.max(maxLen, len1 + len2);
                    }
                    // Or no turn: just take len1
                    maxLen = Math.max(maxLen, len1);
                }
            }
        }
        return maxLen;
    }
}
# @lc code=end