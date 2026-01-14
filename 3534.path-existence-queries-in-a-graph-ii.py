#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict
        
        # Build adjacency list using sets to avoid duplicates
        graph = defaultdict(set)
        
        # Sort nodes by their values to efficiently find neighbors
        sorted_nodes = sorted(range(n), key=lambda x: nums[x])
        
        # For each node, connect to nodes within maxDiff
        for i in range(n):
            node = sorted_nodes[i]
            # Look forward in sorted order
            j = i + 1
            while j < n and nums[sorted_nodes[j]] - nums[node] <= maxDiff:
                neighbor = sorted_nodes[j]
                graph[node].add(neighbor)
                graph[neighbor].add(node)
                j += 1
        
        def bfs(start, end):
            if start == end:
                return 0
            
            visited = set([start])
            queue = deque([(start, 0)])
            
            while queue:
                curr, dist = queue.popleft()
                
                for neighbor in graph[curr]:
                    if neighbor == end:
                        return dist + 1
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
            
            return -1
        
        result = []
        for u, v in queries:
            result.append(bfs(u, v))
        
        return result
# @lc code=end