#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(a: List[int], b: List[int]) -> int:
            return len(set(a) & set(b))

        n = len(properties)
        visited = [False] * n
        adjacency_list = {i: [] for i in range(n)}
        
        # Building the adjacency list based on intersection condition
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
        
        # Counting connected components using DFS traversal
        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        return count # @lc code=end