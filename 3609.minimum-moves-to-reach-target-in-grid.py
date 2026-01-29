#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        moves = 0
        while tx != sx or ty != sy:
            if tx < sx or ty < sy:
                return -1
            if tx > ty:
                if ty == sy:
                    return moves + (tx - sx) // ty if (tx - sx) % ty == 0 else -1
                tx -= max((tx - sx) // ty * ty, ty)
            else:
                if tx == sx:
                    return moves + (ty - sy) // tx if (ty - sy) % tx == 0 else -1
                ty -= max((ty - sy) // tx * tx, tx)
            moves += 1
        return moves
# @lc code=end