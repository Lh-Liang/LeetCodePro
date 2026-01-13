#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)
        
        # Precompute distances
        dist = [[0] * n for _ in range(n)]
        all_distances = set()
        for i in range(n):
            for j in range(i+1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i][j] = dist[j][i] = d
                all_distances.add(d)
        
        all_distances = sorted(all_distances, reverse=True)
        
        def can_select(min_dist):
            def backtrack(index, selected):
                if len(selected) == k:
                    return True
                if index == n:
                    return False
                if n - index + len(selected) < k:
                    return False
                
                # Try selecting current point
                can_select_current = all(
                    dist[index][sel_idx] >= min_dist
                    for sel_idx in selected
                )
                
                if can_select_current:
                    selected.append(index)
                    if backtrack(index + 1, selected):
                        return True
                    selected.pop()
                
                # Try not selecting current point
                return backtrack(index + 1, selected)
            
            return backtrack(0, [])
        
        # Try all distances from largest to smallest
        for d in all_distances:
            if can_select(d):
                return d
        
        return 0
# @lc code=end