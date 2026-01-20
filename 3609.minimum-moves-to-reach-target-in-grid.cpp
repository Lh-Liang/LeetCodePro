#
# @lc app=leetcode id=3609 lang=cpp
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution {
public:
    int minMoves(int sx, int sy, int tx, int ty) {
        // If target is smaller than start, impossible
        if (tx < sx || ty < sy) return -1;
        
        int moves = 0;
        
        // While both coordinates are larger than start
        while (tx > sx && ty > sy) {
            if (tx > ty) {
                if (tx % 2 == 0 && tx / 2 >= ty) {
                    tx /= 2;
                    moves++;
                } else {
                    tx -= ty;
                    moves++;
                }
            } else if (ty > tx) {
                if (ty % 2 == 0 && ty / 2 >= tx) {
                    ty /= 2;
                    moves++;
                } else {
                    ty -= tx;
                    moves++;
                }
            } else {
                // tx == ty
                // Can only be reached from (0, ty) or (tx, 0)
                // If sx == 0, we can reduce tx. If sy == 0, we can reduce ty.
                if (sx == 0) {
                    tx -= ty;
                    moves++;
                } else if (sy == 0) {
                    ty -= tx;
                    moves++;
                } else {
                    return -1;
                }
            }
        }
        
        // Now we are at the boundary for at least one coordinate
        if (tx == sx) {
            while (ty > sy) {
                if (ty > tx) {
                    if (ty % 2 == 0 && ty / 2 >= tx) {
                        ty /= 2;
                        moves++;
                    } else {
                        ty -= tx;
                        moves++;
                    }
                } else {
                    // ty <= tx
                    // We can only subtract tx. 
                    ty -= tx;
                    moves++;
                }
            }
            if (ty != sy) return -1;
        } else if (ty == sy) {
            while (tx > sx) {
                if (tx > ty) {
                    if (tx % 2 == 0 && tx / 2 >= ty) {
                        tx /= 2;
                        moves++;
                    } else {
                        tx -= ty;
                        moves++;
                    }
                } else {
                    // tx <= ty
                    tx -= ty;
                    moves++;
                }
            }
            if (tx != sx) return -1;
        } else {
            // Should not happen if loop logic is correct and we return -1 on impossible tx==ty
            return -1;
        }
        
        return moves;
    }
};
# @lc code=end