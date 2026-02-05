#
# @lc app=leetcode id=3609 lang=java
#
# [3609] Minimum Moves to Reach Target in Grid
#
# @lc code=start
class Solution {
    public int minMoves(int sx, int sy, int tx, int ty) {
        int moves = 0;
        while (tx > sx && ty > sy) {
            if (tx > ty) {
                if (ty == 0) return -1;
                int times = Math.max(1, (tx - sx) / ty);
                tx -= times * ty;
                moves += times;
            } else {
                if (tx == 0) return -1;
                int times = Math.max(1, (ty - sy) / tx);
                ty -= times * tx;
                moves += times;
            }
            // After move, verify we haven't gone below start
            if (tx < sx || ty < sy) return -1;
        }
        // Check if we landed exactly at start
        if (tx == sx && ty == sy) return moves;
        // If only one coordinate matches, check if the other can be reached in valid moves
        if (tx == sx && ty > sy && sx != 0 && (ty - sy) % sx == 0) {
            moves += (ty - sy) / sx;
            return moves;
        }
        if (ty == sy && tx > sx && sy != 0 && (tx - sx) % sy == 0) {
            moves += (tx - sx) / sy;
            return moves;
        }
        return -1;
    }
}
# @lc code=end