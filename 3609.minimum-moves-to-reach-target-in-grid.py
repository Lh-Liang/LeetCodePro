#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        # Approach: Work backwards from (tx, ty) to (sx, sy)
        moves = 0
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty # Reduce tx if it's larger
            else:
                ty %= tx # Reduce ty if it's larger
        # Check if we can directly reach with remaining moves in one direction
        if sx == tx and sy <= ty and (ty - sy) % sx == 0:
            return moves + (ty - sy) // sx
        elif sy == ty and sx <= tx and (tx - sx) % sy == 0:
            return moves + (tx - sx) // sy
        return -1 # If not possible to reach exactly
# @lc code=end