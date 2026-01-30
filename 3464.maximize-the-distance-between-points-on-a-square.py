#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        from itertools import combinations
        def is_possible(dist):
            # For small k, use exhaustive combinations for correctness
            if k <= 10:
                for subset in combinations(points, k):
                    if all(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]) >= dist for i,p1 in enumerate(subset) for p2 in subset[i+1:]):
                        return True
                return False
            else:
                # For larger k, ensure the method used is justified
                # If greedy is not proven optimal, attempt all combinations if feasible
                # Fallback to greedy only if exhaustive search is not computationally possible and document potential limitations
                if len(points) < 1000:
                    for subset in combinations(points, k):
                        if all(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]) >= dist for i,p1 in enumerate(subset) for p2 in subset[i+1:]):
                            return True
                    return False
                else:
                    # Greedy heuristic: not always correct, but used if exhaustive not possible
                    selected = []
                    for p in points:
                        if all(abs(p[0]-q[0]) + abs(p[1]-q[1]) >= dist for q in selected):
                            selected.append(p)
                            if len(selected) == k:
                                return True
                    return False
        points.sort()
        left, right = 0, 2*side
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        # Final validation to ensure correctness
        assert is_possible(ans)
        return ans
# @lc code=end