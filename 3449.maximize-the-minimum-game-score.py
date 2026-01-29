#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        def can_achieve(X: int) -> bool:
            if X == 0: return True
            
            # Target visits for each index
            target = [(X + p - 1) // p for p in points]
            
            moves = 0
            curr_v = [0] * n
            
            # Find the last index that actually needs visits
            # Since X > 0 and points > 0, every index needs >= 1 visit.
            # However, round trips from n-2 might satisfy n-1.
            
            # Start movement: outside to index 0
            moves = 1
            curr_v[0] = 1
            if moves > m: return False
            
            for i in range(n):
                # How many more visits does index i need?
                needed = target[i] - curr_v[i]
                
                if needed > 0:
                    if i == n - 1:
                        # At the last element, we must oscillate with n-2
                        moves += 2 * needed
                    else:
                        # Oscillate with i+1
                        moves += 2 * needed
                        curr_v[i+1] += needed
                
                if moves > m: return False
                
                # Check if we can stop: if we just finished i, and i+1 is the last index
                # and i+1 is already satisfied, we don't need to move to i+1.
                if i == n - 1: 
                    return True
                
                # If the next element and all elements beyond are already satisfied, stop.
                # In this greedy, only i+1 can be non-zero beyond i.
                if i + 1 == n - 1 and curr_v[i+1] >= target[i+1]:
                    return True
                
                # Move to the next index
                moves += 1
                curr_v[i+1] += 1
                if moves > m: return False
                
            return True

        low = 0
        high = 10**15
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
# @lc code=end