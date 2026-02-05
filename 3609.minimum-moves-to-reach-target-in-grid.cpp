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
            if (tx < sx || ty < sy) return -1;
            if (tx >= ty && tx > sx) {
                int m = std::max(tx, ty);
                int jump = std::max(1, (tx - sx) / m);
                tx -= jump * m;
                moves += jump;
            } else if (ty > tx && ty > sy) {
                int m = std::max(tx, ty);
                int jump = std::max(1, (ty - sy) / m);
                ty -= jump * m;
                moves += jump;
            } else {
                return -1;
            }
        }
        return (tx == sx && ty == sy) ? moves : -1;
    }
};
# @lc code=end