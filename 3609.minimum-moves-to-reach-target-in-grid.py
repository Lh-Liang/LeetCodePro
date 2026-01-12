#
# @lc app=leetcode id=3609 lang=python3
#
# [3609] Minimum Moves to Reach Target in Grid
#

# @lc code=start
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx == tx and sy == ty:
            return 0
        
        # Work backwards from (tx, ty) to (sx, sy)
        # If tx > ty, the previous step was (tx - m, ty) where m = max(tx-m, ty)
        # This implies tx - m >= ty, so m = tx - ty. 
        # For this to be valid, tx - ty >= ty => tx >= 2*ty.
        # If tx == ty, it's impossible unless it's the start (handled above)
        # or if one was 0 (e.g., (0, 1) -> (1, 1)).

        ans = 0
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return ans
            
            if tx > ty:
                if ty == 0:
                    # If ty is 0, we can only move if sy is 0 and we subtract tx-sx
                    # But max(x, 0) = x, so (x, 0) -> (2x, 0). 
                    # This is a geometric progression x, 2x, 4x...
                    if sy != 0 or sx == 0: return -1
                    curr = tx
                    while curr > sx:
                        if curr % 2 != 0: return -1
                        curr //= 2
                        ans += 1
                    return ans if curr == sx else -1
                
                # Normal case: tx = x + max(x, ty). Since tx > ty, max(x, ty) must be x.
                # So tx = 2x => x = tx / 2. This only works if tx is even and tx/2 >= ty.
                if tx >= 2 * ty:
                    if tx % 2 != 0: return -1
                    tx //= 2
                    ans += 1
                elif tx > ty:
                    # tx = ty + original_x, where original_x < ty.
                    # Then max(original_x, ty) = ty. So tx = original_x + ty.
                    # original_x = tx - ty.
                    tx -= ty
                    ans += 1
                else:
                    return -1
            elif ty > tx:
                if tx == 0:
                    if sx != 0 or sy == 0: return -1
                    curr = ty
                    while curr > sy:
                        if curr % 2 != 0: return -1
                        curr //= 2
                        ans += 1
                    return ans if curr == sy else -1
                
                if ty >= 2 * tx:
                    if ty % 2 != 0: return -1
                    ty //= 2
                    ans += 1
                elif ty > tx:
                    ty -= tx
                    ans += 1
                else:
                    return -1
            else:
                # tx == ty and not start
                # The only way to get to (m, m) is from (0, m) or (m, 0)
                if sx == 0 and sy == tx:
                    # Check if we can reach (0, tx) then one move to (tx, tx)
                    # Actually, the loop handles (0, tx)
                    ty -= tx # move to (tx, 0)
                    ans += 1
                elif sy == 0 and sx == ty:
                    tx -= ty
                    ans += 1
                else:
                    return -1
        
        return -1
# @lc code=end