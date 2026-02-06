#
# @lc app=leetcode id=3609 lang=java
#
# [3609] Minimum Moves to Reach Target in Grid
#
# @lc code=start
class Solution {
    public int minMoves(int sx, int sy, int tx, int ty) {
        int moves = 0;
        while (tx > sx || ty > sy) {
            if (tx < sx || ty < sy) return -1;
            if (tx > ty) {
                int m = Math.max(tx, ty);
                int prev_tx = Math.max(sx, ty);
                // Reduce as much as possible in one step
                int jump = (tx - sx - 1) / m + 1;
                if (ty == sy) jump = 1;
                tx -= m * jump;
                moves += jump;
            } else if (ty > tx) {
                int m = Math.max(tx, ty);
                int prev_ty = Math.max(tx, sy);
                int jump = (ty - sy - 1) / m + 1;
                if (tx == sx) jump = 1;
                ty -= m * jump;
                moves += jump;
            } else {
                // tx == ty
                if (tx == sx && ty == sy) return moves;
                return -1;
            }
        }
        return (tx == sx && ty == sy) ? moves : -1;
    }
}
# @lc code=end