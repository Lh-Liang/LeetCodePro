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
                tx %= ty;
            } else {
                ty %= tx;
            }
            moves++;
        }
        if (tx == sx && sy <= ty && (ty - sy) % sx == 0) {
            return moves + (ty - sy) / sx;
        } else if (ty == sy && sx <= tx && (tx - sx) % sy == 0) {
            return moves + (tx - sx) / sy;
        }
        return -1;
    }
}
# @lc code=end