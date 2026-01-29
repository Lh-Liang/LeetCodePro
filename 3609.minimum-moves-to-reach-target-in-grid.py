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
                # Unique predecessor logic for tx > ty
                if tx >= 2 * ty:
                    if tx % 2 != 0:
                        return -1
                    tx //= 2
                else:
                    tx -= ty
                moves += 1
            elif ty > tx:
                # Unique predecessor logic for ty > tx
                if ty >= 2 * tx:
                    if ty % 2 != 0:
                        return -1
                    ty //= 2
                else:
                    ty -= tx
                moves += 1
            else:
                # tx == ty. This can only be reached from (0, tx) or (tx, 0)
                # Check if target is reachable from sx, sy via one of these
                if sx == 0 and sy == ty:
                    # Already handled by the while condition and tx==sx check
                    pass 
                elif sy == 0 and sx == tx:
                    pass
                elif sx == 0 and tx > 0:
                    tx = 0
                    moves += 1
                    continue
                elif sy == 0 and ty > 0:
                    ty = 0
                    moves += 1
                    continue
                return -1
                
        return -1
# @lc code=end