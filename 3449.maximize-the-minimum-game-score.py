#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)
        
        # We need at least n moves to visit all positions
        if m < n:
            return 0
        
        def can_achieve(target):
            if target == 0:
                return True
            total_visits = sum((target + points[i] - 1) // points[i] for i in range(n))
            return total_visits <= m
        
        # Binary search on the minimum score
        left, right = 0, m * max(points)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
# @lc code=end