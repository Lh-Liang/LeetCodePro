#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        def check(target):
            if target == 0:
                return True
            
            moves = 0
            # extra_hits[i] is the number of times index i was hit 
            # because we toggled between i-1 and i to satisfy i-1.
            extra_hits = 0
            
            for i in range(n):
                # We need to reach target / points[i] hits
                needed_hits = (target + points[i] - 1) // points[i]
                
                # Current hits at i = hits from toggling (i-1, i) + 1 (the move to i)
                # But we only move to i if we haven't finished the array or i needs more hits.
                # Exception: Index 0 always needs a move from -1.
                
                actual_hits = extra_hits
                
                if i == n - 1 and actual_hits >= needed_hits:
                    # We don't need to move to the last element if it's already satisfied
                    break
                
                # Move to index i
                moves += 1
                actual_hits += 1
                
                if moves > m:
                    return False
                
                if actual_hits < needed_hits:
                    remain = needed_hits - actual_hits
                    # To get 'remain' more hits at i, we toggle i <-> i+1 'remain' times
                    # unless i is the last element, then we toggle i <-> i-1.
                    if i < n - 1:
                        moves += 2 * remain
                        extra_hits = remain
                    else:
                        moves += 2 * remain
                        # No next element to pass extra hits to
                else:
                    extra_hits = 0
                
                if moves > m:
                    return False
            
            return moves <= m

        low, high = 0, 10**18
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
# @lc code=end