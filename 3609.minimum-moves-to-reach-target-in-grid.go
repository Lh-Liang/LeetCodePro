#
# @lc app=leetcode id=3609 lang=golang
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
func minMoves(sx int, sy int, tx int, ty int) int {
    moves := 0
    // Reverse approach: reduce tx or ty until reaching sx or sy
    for tx > sx && ty > sy {
        if tx > ty {
            if tx%ty == 0 {
                return -1 // no valid path exists if remainder is zero and not matching exactly
            }
            tx %= ty // reduce larger by smaller
        } else {
            if ty%tx == 0 {
                return -1 // no valid path exists if remainder is zero and not matching exactly
            }
            ty %= tx // reduce larger by smaller
        }
        moves++
    }
    // Check if one coordinate has reached and can be used to align the other
    if sx == tx && sy <= ty && (ty-sy)%sx == 0 {
        return moves + (ty-sy)/sx 
    } else if sy == ty && sx <= tx && (tx-sx)%sy == 0 {
        return moves + (tx-sx)/sy 
    } else {
        return -1 
    }
}
# @lc code=end