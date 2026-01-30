#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        left, right = 0, 2 * side
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            graph = {i: [] for i in range(len(points))}
            
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    if manhattan_distance(points[i], points[j]) >= mid:
                        graph[i].append(j)
                        graph[j].append(i)
            
            def can_select_k_points():
                visited = set()
                def dfs(node):
                    stack = [node]
                    component_size = 0
                    while stack:
                        current = stack.pop()
                        if current not in visited:
                            visited.add(current)
                            component_size += 1
                            stack.extend(graph[current])
                    return component_size >= k
                return any(dfs(node) for node in range(len(points)) if node not in visited)
            
            if can_select_k_points():
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer # @lc code=end