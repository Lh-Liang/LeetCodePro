#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def is_possible(x):
            # For each i, how many times do we need to visit it to reach at least x?
            # Each visit adds points[i]
            from math import ceil
            total_moves = 0
            for p in points:
                total_moves += ceil(x / p)
            return total_moves <= m

        left, right = 0, max(points) * m
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
# @lc code=end