#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def canSelectWithDistance(min_dist):
            # Greedy selection attempt for verifying the minimal required distance
            selected = []
            for point in points:
                if not selected or all(abs(px - x) + abs(py - y) >= min_dist for (px, py) in selected):
                    selected.append(point)
                    if len(selected) == k:
                        return True
            return False
        
        low, high = 0, 2 * side  # max possible manhattan distance in square with side 'side'
        while low < high:
            mid = (low + high + 1) // 2
            if canSelectWithDistance(mid):
                low = mid  # try for larger distances
            else:
                high = mid - 1
        return low
# @lc code=end