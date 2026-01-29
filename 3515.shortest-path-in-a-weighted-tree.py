#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        # Create adjacency list for the tree and initial edge weights map
        graph = defaultdict(list)
        edge_weights = {}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            edge_weights[(min(u,v), max(u,v))] = w
        
        # Function to perform BFS and calculate distances from root (1)
        def bfs_distances(root: int) -> List[int]:
            distances = [-1] * (n + 1)
            distances[root] = 0
            queue = deque([root])
            while queue:
                current = queue.popleft()
                current_distance = distances[current]
                for neighbor, weight in graph[current]:
                    if distances[neighbor] == -1:  # Not visited yet
                        distances[neighbor] = current_distance + weight
                        queue.append(neighbor)
            return distances
        
        # Initialize distances from root using BFS
        distances = bfs_distances(1)
        answers = []  # To store results of type-2 queries
        
        # Process each query sequentially 
        for query in queries:
            if query[0] == 1:  # Update query [1,u,v,w']
                _, u, v, new_weight = query 
                u, v = min(u,v), max(u,v)  # Ensure consistent order for edge key use
                old_weight = edge_weights[(u,v)]
                if old_weight != new_weight:
                    edge_weights[(u,v)] = new_weight
                    # Adjust affected paths efficiently (this part would be optimized with advanced techniques)
graph[u].remove((v, old_weight))
graph[v].remove((u, old_weight))
graph[u].append((v, new_weight))
graph[v].append((u, new_weight))
distances = bfs_distances(1)  # Recompute efficiently (targeted optimization required)
elif query[0] == 2:    # Compute shortest path distance type [2,x]
x = query[1]	answers.append(distances[x])    return answers    	# @lc code=end