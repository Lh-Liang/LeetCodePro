#
# @lc app=leetcode id=3449 lang=python3
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def canAchieve(min_score):
            # This function checks if we can achieve at least min_score in all gameScore entries with m moves
            total_moves_needed = 0
            for point in points:
                # Calculate additional moves needed if current point is less than min_score
                if point < min_score:
                    total_moves_needed += min_score - point
                # If at any point, required moves exceed available moves, return False
                if total_moves_needed > m:
                    return False
            return True
        
        # Set initial boundaries for binary search based on problem constraints and logic reasoning
        low, high = min(points), max(points) + m // len(points)
        
        while low < high:
            mid = (low + high + 1) // 2
            if canAchieve(mid):
                low = mid  # Narrow down to upper half if achievable
            else:
                high = mid - 1  # Narrow down to lower half if not achievable
        
        return low  # Return the highest possible minimum score found within move constraints
# @lc code=end