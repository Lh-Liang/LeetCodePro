#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        adjacency_list = [[] for _ in range(n)]
        
        # Define intersect function
        def intersect(a, b):
            return len(set(a) & set(b))
        
        # Construct adjacency list
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)
        
        # Find connected components using DFS
        visited = [False] * n
        
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in adjacency_list[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        # Count connected components
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
                visited[i] = True # Ensure marking as visited after DFS call to avoid revisiting. 
        return count  "}