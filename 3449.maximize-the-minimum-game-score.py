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
            
            cur_moves = 0
            # extra_visits_next tracks the number of times we visit the *next* index (i+1)
            # as a side effect of performing back-and-forth moves at the current index i
            # to satisfy the target score at i.
            extra_visits_next = 0 
            
            for i in range(n):
                # Every step i takes at least 1 move to reach from i-1 (or start)
                cur_moves += 1
                
                # Base visits is 1 (arrival from left) + side-effect visits from i-1
                visits = 1 + extra_visits_next
                
                current_score = visits * points[i]
                needed_cycles = 0
                
                if current_score < target:
                    deficit = target - current_score
                    # Ceiling division to find how many more visits we need
                    needed_cycles = (deficit + points[i] - 1) // points[i]
                    
                    # Each cycle (i -> i+1 -> i) costs 2 moves
                    cur_moves += 2 * needed_cycles
                
                # If we are not at the last element, the cycles i -> i+1 -> i 
                # contribute 'needed_cycles' visits to i+1.
                # If we are at the last element, the cycles are (n-1) -> (n-2) -> (n-1),
                # which do not affect any 'next' element. 
                # Since the loop ends after this, updating extra_visits_next is harmless but unused.
                extra_visits_next = needed_cycles
                
                if cur_moves > m:
                    return False
            
            return True

        # Binary Search for the maximum minimum score
        # Lower bound is 0.
        # Upper bound estimation: Max points is 10^6, max moves 10^9.
        # In the best case, we dump all moves on the largest point -> 10^15.
        # We use a safe upper bound.
        left, right = 0, 2 * 10**15 
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
# @lc code=end