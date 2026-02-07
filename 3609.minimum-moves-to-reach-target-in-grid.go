#
# @lc app=leetcode id=3609 lang=golang
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
func minMoves(sx int, sy int, tx int, ty int) int {
    moves := 0
    for tx > sx || ty > sy {
        if tx < sx || ty < sy {
            return -1
        }
        if tx > ty {
            m := ty
            if m == 0 {
                return -1
            }
            tx -= m
        } else if ty > tx {
            m := tx
            if m == 0 {
                return -1
            }
            ty -= m
        } else { // tx == ty
            // If both coordinates equal but don't match start, it's impossible
            break
        }
        moves++
    }
    if tx == sx && ty == sy {
        return moves
    }
    return -1
}
# @lc code=end