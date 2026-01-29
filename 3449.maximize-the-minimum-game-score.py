#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)
        
        def check(X):
            if X == 0:
                return True
            
            moves = 0
            prev_extra = 0
            for i in range(n):
                # Calculate visits needed for current index i
                needed_i = (X + points[i] - 1) // points[i]
                
                # Every index i requires a move from i-1 to i (except the first start at -1)
                moves += 1
                if moves > m:
                    return False
                
                # v_i: visits to i so far (1 from current move + prev_extra from i-1 back-and-forth)
                v_i = prev_extra + 1
                rem = max(0, needed_i - v_i)
                
                # To get 'rem' more visits, move i -> i+1 -> i 'rem' times.
                # Each pair adds 1 visit to i and 1 visit to i+1.
                moves += 2 * rem
                if moves > m:
                    return False
                
                # If this is the last index, all requirements are satisfied.
                if i == n - 1:
                    return True
                
                # Shortcut: if the next index is the last and already satisfied by rem moves,
                # we stop here without taking the final move to i+1.
                needed_next = (X + points[i+1] - 1) // points[i+1]
                if i == n - 2 and rem >= needed_next:
                    return True
                
                # Carry over the 'rem' visits to the next index.
                prev_extra = rem
            
            return True

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