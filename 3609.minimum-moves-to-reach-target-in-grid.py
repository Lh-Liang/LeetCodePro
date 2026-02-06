#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        moves = 0
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return moves
            if tx > ty:
                if ty == sy:
                    # Reduce directly by subtracting multiples of y
                    return moves + (tx - sx) // ty if (tx - sx) % ty == 0 else -1
                tx %= ty
            else:
                if tx == sx:
                    # Reduce directly by subtracting multiples of x
                    return moves + (ty - sy) // tx if (ty - sy) % tx == 0 else -1
                ty %= tx
            moves += 1
        return -1 # If we exit loop without matching starting coordinates exactly
# @lc code=end