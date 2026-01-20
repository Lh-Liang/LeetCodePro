import math

class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        moves = 0
        
        # Helper to check power of two
        def is_power_of_two(n):
            return n > 0 and (n & (n - 1)) == 0
        
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return moves
            
            if tx > ty:
                # If we are in a state where y matches sy, and sx is larger than ty,
                # we are purely in the doubling regime for x. We can fast-forward.
                if ty == sy and sx > ty:
                    if tx % sx == 0 and is_power_of_two(tx // sx):
                        return moves + (tx // sx).bit_length() - 1
                    else:
                        return -1

                if tx >= 2 * ty:
                    # Must have come from doubling x
                    if tx % 2 != 0:
                        return -1
                    tx //= 2
                    moves += 1
                else:
                    # Must have come from x + y
                    tx -= ty
                    moves += 1
            elif ty > tx:
                # Symmetric logic for y
                if tx == sx and sy > tx:
                    if ty % sy == 0 and is_power_of_two(ty // sy):
                        return moves + (ty // sy).bit_length() - 1
                    else:
                        return -1

                if ty >= 2 * tx:
                    if ty % 2 != 0:
                        return -1
                    ty //= 2
                    moves += 1
                else:
                    ty -= tx
                    moves += 1
            else:
                # tx == ty
                # Can only reach equal coordinates from a state where one coordinate is 0.
                # e.g. (0, y) -> (y, y) or (x, 0) -> (x, x)
                res = float('inf')
                
                # Check possibility coming from x=0
                if sx == 0:
                    # We need to check distance from (0, sy) to (0, ty)
                    # This path is purely doubling y
                    if ty == sy:
                         res = min(res, moves + 1)
                    elif sy > 0 and ty % sy == 0 and is_power_of_two(ty // sy):
                         res = min(res, moves + 1 + (ty // sy).bit_length() - 1)
                    # If sy == 0, we can only reach (0, ty) if ty == 0, but we are at tx=ty>0 here usually
                    # (unless tx=ty=0 which is caught at start)
                    
                # Check possibility coming from y=0
                if sy == 0:
                    # Check distance from (sx, 0) to (tx, 0)
                    if tx == sx:
                        res = min(res, moves + 1)
                    elif sx > 0 and tx % sx == 0 and is_power_of_two(tx // sx):
                        res = min(res, moves + 1 + (tx // sx).bit_length() - 1)
                
                if res != float('inf'):
                    return res
                else:
                    return -1
                    
        return -1