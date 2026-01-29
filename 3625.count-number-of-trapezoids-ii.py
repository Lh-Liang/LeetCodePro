# @lc code=start
from typing import List
from itertools import combinations

def slope(p1, p2):
    # Handling vertical lines by returning None as slope
    if p1[0] == p2[0]:
        return None
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        seen_trapezoids = set()
        for quad in combinations(points, 4):
            # Calculate slopes for each pair to find parallels
            slopes = {}
            for i in range(4):
                for j in range(i + 1, 4):
                    s = slope(quad[i], quad[j])
                    if s not in slopes:
                        slopes[s] = [(i, j)]
                    else:
                        slopes[s].append((i, j))
            # Check if there is at least one pair of parallel sides
            for s in slopes:
                if len(slopes[s]) > 1:
                    # Found parallel sides, record the trapezoid uniquely
                    trapezoid_points = tuple(sorted(quad))
                    seen_trapezoids.add(trapezoid_points)
                    break
        return len(seen_trapezoids)
# @lc code=end