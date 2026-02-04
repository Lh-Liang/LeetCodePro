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
        while (tx >= sx && ty >= sy) {
            if (tx > ty) {
                if (ty > sy) {
                    tx %= ty;
                } else {
                    // Check if remaining difference can be covered by multiples of max value.
                    return ((tx - sx) % ty == 0) ? moves + (tx - sx) / ty : -1;
                }
            } else {
                if (tx > sx) {
                    ty %= tx;
                } else {
                    // Check if remaining difference can be covered by multiples of max value.
                    return ((ty - sy) % tx == 0) ? moves + (ty - sy) / tx : -1;
                }
            }
            ++moves; // Increment move count for each successful reduction step.
        }
        return -1; // If unable to reduce successfully to start points, return impossible.
    } 
}; 
# @lc code=end