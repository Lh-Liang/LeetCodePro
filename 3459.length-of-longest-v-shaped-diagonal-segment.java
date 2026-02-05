#
# @lc app=leetcode id=3459 lang=java
#
# [3459] Length of Longest V-Shaped Diagonal Segment
#
# @lc code=start
class Solution {
    private static final int[][] DIRS = {
        {1, 1},   // ↘
        {1, -1},  // ↙
        {-1, -1}, // ↖
        {-1, 1}   // ↗
    };
    // Clockwise turn mapping: 0→1, 1→2, 2→3, 3→0
    private static final int[] TURN = {1, 2, 3, 0};
    private int n, m;
    private int[][] grid;
    private int maxLen;
    private Integer[][][][][] memo;
    // Alternation: expectedVals[0] = 2, expectedVals[1] = 0
    private static final int[] expectedVals = {2, 0};

    public int lenOfVDiagonal(int[][] grid) {
        this.n = grid.length;
        this.m = grid[0].length;
        this.grid = grid;
        this.maxLen = 0;
        this.memo = new Integer[n][m][4][2][2]; // x, y, dir, parity, turned
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    for (int dir = 0; dir < 4; ++dir) {
                        maxLen = Math.max(maxLen, dfs(i, j, dir, 1, 0, 0));
                    }
                }
            }
        }
        return maxLen;
    }

    private int dfs(int x, int y, int dir, int len, int parity, int turned) {
        if (memo[x][y][dir][parity][turned] != null) {
            return memo[x][y][dir][parity][turned] + len - 1;
        }
        int res = len;
        int nx = x + DIRS[dir][0];
        int ny = y + DIRS[dir][1];
        int nextExpected = expectedVals[parity];
        if (inGrid(nx, ny) && grid[nx][ny] == nextExpected) {
            res = Math.max(res, dfs(nx, ny, dir, len + 1, parity ^ 1, turned));
        }
        // Try to turn if not turned yet
        if (turned == 0) {
            int ndir = TURN[dir];
            int tx = x + DIRS[ndir][0];
            int ty = y + DIRS[ndir][1];
            if (inGrid(tx, ty) && grid[tx][ty] == nextExpected) {
                res = Math.max(res, dfs(tx, ty, ndir, len + 1, parity ^ 1, 1));
            }
        }
        memo[x][y][dir][parity][turned] = res - len + 1;
        return res;
    }

    private boolean inGrid(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }
}
# @lc code=end