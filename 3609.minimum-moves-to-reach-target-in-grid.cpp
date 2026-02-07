#
# @lc app=leetcode id=3609 lang=cpp
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution {
public:
    int minMoves(int sx, int sy, int tx, int ty) {
        int moves = 0;
        while ((tx > sx && ty > sy) || tx > sx || ty > sy) {
            if (tx > ty) {
                if (ty == sy) {
                    return (tx - sx) % ty == 0 ? moves + ((tx - sx) / ty) : -1;
                }
                tx %= ty;
            } else {
                if (tx == sx) {
                    return (ty - sy) % tx == 0 ? moves + ((ty - sy) / tx) : -1;
                }
                ty %= tx;
            }
            ++moves;
        }
        return (tx == sx && ty == sy) ? moves : -1;
    }
};
# @lc code=end