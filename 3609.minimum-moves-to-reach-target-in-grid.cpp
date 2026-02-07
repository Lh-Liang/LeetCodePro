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
        while (tx > sx && ty > sy) {
            if (tx > ty) {
                tx -= max(1, tx - sx);
            } else {
                ty -= max(1, ty - sy);
            }
            moves++;
        }
        return (tx == sx && ty == sy) ? moves : -1;
    }
};
# @lc code=end