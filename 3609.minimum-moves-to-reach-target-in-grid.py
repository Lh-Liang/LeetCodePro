#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        moves = 0
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
            moves += 1
        if (tx == sx and (ty - sy) % tx == 0) or (ty == sy and (tx - sx) % ty == 0):
            return moves + max((ty - sy) // tx, (tx - sx) // ty)
        return -1
# @lc code=end