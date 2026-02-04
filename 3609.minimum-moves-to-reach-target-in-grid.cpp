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
        while (tx > sx || ty > sy) {
            if (tx == ty) {
                // If coordinates are equal but not at start, impossible to progress
                return -1;
            } else if (tx > ty) {
                if (ty < sy) return -1;
                tx -= ty;
            } else { // ty > tx
                if (tx < sx) return -1;
                ty -= tx;
            }
            moves++;
        }
        return (tx == sx && ty == sy) ? moves : -1;
    }
};
# @lc code=end