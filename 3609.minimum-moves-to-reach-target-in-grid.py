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
            # Reverse move logic: Reduce larger coordinate by smaller one
            if tx > ty:
                tx -= ty  # Reverse move that would have increased y
            else:
                ty -= tx  # Reverse move that would have increased x
            moves += 1
        # Final checks for exact match along one dimension
        if sx == tx and sy <= ty and (ty - sy) % sx == 0:
            return moves + (ty - sy) // sx
        elif sy == ty and sx <= tx and (tx - sx) % sy == 0:
            return moves + (tx - sx) // sy
        return -1
# @lc code=end