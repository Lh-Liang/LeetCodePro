#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Use binary search to find the maximum possible minimum distance
        def canPlacePoints(min_dist):
            # Strategic approach to place points with at least `min_dist` spacing
            count = 0
            last_point = None
            for point in sorted_points:
                if last_point is None or abs(point[0] - last_point[0]) + abs(point[1] - last_point[1]) >= min_dist:
                    count += 1
                    last_point = point
                    if count == k:
                        return True
            return False
        
        # Sort points based on their positions along square boundaries (e.g., clockwise)
        sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
        low, high = 0, 2 * side  # Max distance can be diagonal of square side length * sqrt(2) ~ side*2 max manhattan distance
        while low < high:
            mid = (low + high + 1) // 2
            if canPlacePoints(mid):
                low = mid  # Try for a larger minimum distance
            else:
                high = mid - 1  # Reduce the distance if not possible to place all k points
        return low
# @lc code=end