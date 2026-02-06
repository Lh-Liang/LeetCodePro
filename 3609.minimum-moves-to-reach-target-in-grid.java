#
# @lc app=leetcode id=3609 lang=java
#
# [3609] Minimum Moves to Reach Target in Grid
#
# @lc code=start
class Solution {
    public int minMoves(int sx, int sy, int tx, int ty) {
        int moves = 0;
        while (tx >= sx && ty >= sy) {
            if (tx == sx && ty == sy) return moves;
            if (tx > ty) {
                if (ty > sy) tx %= ty;
                else return ((tx - sx) % ty == 0) ? moves + (tx - sx) / ty : -1;
            } else {
                if (tx > sx) ty %= tx;
                else return ((ty - sy) % tx == 0) ? moves + (ty - sy) / tx : -1;
            }
            moves++;
        }
        return -1;
    }
}
# @lc code=end