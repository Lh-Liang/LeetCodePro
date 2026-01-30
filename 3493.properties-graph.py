#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(a, b):
            return len(set(a) & set(b))
        
        n = len(properties)
        visited = [False] * n
        adjacency_list = {i: [] for i in range(n)}
        
        # Constructing adjacency list based on intersection logic
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in adjacency_list[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                    
        # Counting connected components
        component_count = 0
        for i in range(n):
            if not visited[i]:
                component_count += 1
                visited[i] = True
                dfs(i)
                
        return component_count
# @lc code=end